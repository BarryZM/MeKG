import time

from sqlalchemy import Table
import re
from .model import CerebrovascularDiseases, CDtoC, Base
from .pg_connection import new_connection
from .scrapy_message import ScrapyMe
from .util.translate import translate


class ScrapyHtml(object):

    def __init__(self, engine, session):
        self.engine = engine
        self.session = session

    def select_all_url(self):
        """
            拿到CerebrovascularDiseases所有英文数据
        """
        return self.session.query(CerebrovascularDiseases).order_by(CerebrovascularDiseases.rank).all()

    def scrapy(self):
        """
            根据csv内容爬取 url 中详细内容
        """
        me = self.select_all_url()
        sm = ScrapyMe()
        for i in me:
            url = i.url
            if i.studyDescription or i.studyDesign or i.armsandInterventions or i.outcomeMeasuresII or i.groupsandCohorts or i.eligibilityCriteria or i.contactsandLocaons or i.moreInformation:
                continue
            result = sm.scrapy_mess(url)
            i.studyDescription = result.get('studyDescription')
            i.studyDesign = result.get('studyDesign')
            i.armsandInterventions = result.get('armsandInterventions')
            i.outcomeMeasuresII = result.get('outcomeMeasures')
            i.groupsandCohorts = result.get('groupsandCohorts')
            i.eligibilityCriteria = result.get('eligibilityCriteria')
            i.contactsandLocaons = result.get('contactsandLocaons')
            i.moreInformation = result.get('moreInformation')
            try:
                self.session.commit()
                print(f'url:{url} is ok !')
            except Exception as err:
                with open('error.txt', 'a') as f:
                    f.write(f'error: {err},url:{url}')
                print(f'error: {err},url:{url}')
        self.session.close()

    def translate(self):
        """
            利用有道API 翻译英文并存储
        """
        if 'cerebrovascularc' in self.engine.table_names():
            table = Table("cerebrovascularc", Base.metadata, autoload=True)
            table.drop(self.engine)
        CDtoC.metadata.create_all(self.engine)
        # if 'cerebrovascularc' not in self.engine.table_names():
        #     CDtoC.metadata.create_all(self.engine)
        tra_rank = [i.nctNumber for i in self.session.query(CDtoC).order_by(CDtoC.rank).all()]
        me = self.select_all_url()
        for i in me:
            if i.nctNumber in tra_rank:
                continue
            t = CDtoC(nctNumber=i.nctNumber, acronym=i.acronym, enrollment=i.enrollment, otherIDs=i.otherIDs,
                      startDate=i.startDate, primaryCompletionDate=i.primaryCompletionDate,
                      completionDate=i.completionDate, firstPosted=i.firstPosted,
                      resultsFirstPosted=i.resultsFirstPosted, lastUpdatePosted=i.lastUpdatePosted, url=i.url)
            if i.title:
                t.title = translate(i.title)
                # print(t.title)
            if i.status:
                t.status = translate(i.status)
                # print(t.status)
            if i.studyResults:
                t.studyResults = translate(i.studyResults)
                # print(t.studyResults)
            if i.conditions:
                t.conditions = translate(i.conditions)
                # print(t.conditions)
            if i.interventions:
                t.interventions = translate(i.interventions)
                # print(t.interventions)
            if i.outcomeMeasures:
                t.outcomeMeasures = translate(i.outcomeMeasures)
                # print(t.outcomeMeasures)
            if i.sponsorCollaborators:
                t.sponsorCollaborators = translate(i.sponsorCollaborators)
                # print(t.sponsorCollaborators)
            if i.gender:
                t.gender = translate(i.gender)
                # print(t.gender)
            if i.age:
                t.age = translate(i.age)
                # print(t.age)
            if i.phases:
                t.phases = translate(i.phases)
                # print(t.phases)
            if i.fundedBys:
                t.fundedBys = translate(i.fundedBys)
                # print(t.fundedBys)
            if i.studyType:
                t.studyType = translate(i.studyType)
                # print(t.studyType)
            if i.studyDesigns:
                t.studyDesigns = translate(i.studyDesigns)
                # print(t.studyDesigns)
            if i.locations:
                t.locations = translate(i.locations)
            if i.studyDocuments:
                t.studyDocuments = translate(i.studyDocuments)
            if i.studyDescription:
                # ts = re.sub(r'\n', '|', i.studyDescription)
                # for j in ts.split('.'):
                #     print(translate(j))
                t.studyDescription = translate(i.studyDescription)
                # print(ts)
                # print(t.studyDescription)
            if i.studyDesign:
                t.studyDesign = translate(i.studyDesign)
            if i.armsandInterventions:
                t.armsandInterventions = translate(i.armsandInterventions)
            if i.outcomeMeasuresII:
                t.outcomeMeasuresII = translate(i.outcomeMeasuresII)
            if i.groupsandCohorts:
                t.groupsandCohorts = translate(i.groupsandCohorts)
            if i.eligibilityCriteria:
                t.eligibilityCriteria = translate(i.eligibilityCriteria)
            if i.contactsandLocaons:
                t.contactsandLocaons = translate(i.contactsandLocaons)
            if i.moreInformation:
                t.moreInformation = translate(i.moreInformation)
            self.session.add(t)
            try:
                self.session.commit()
                print(f'success {i.rank}')
            except Exception as err:
                with open('error1.txt', 'r') as f:
                    f.write(f'error: {err},url:{i.url}')
                print(err)
            # break


if __name__ == '__main__':
    engine, session = new_connection()
    sh = ScrapyHtml(engine, session)
    sh.scrapy()
    print("scrapy finished !")
    # sh.translate()
