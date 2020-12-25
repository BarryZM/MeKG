"""
    将本地数据库爬取的数据上传到服务器数据库
"""
from sqlalchemy import Table

from scrapy_cerebrovascular.model import CerebrovascularDiseases, Base
from properties import BIT_URI, SQLALCHEMY_DATABASE_URI
from util.pg_connection import connection


class LocalToServer(object):
    def __init__(self, u1, u2):
        self.local_url = u1
        self.server_url = u2

    def go(self):
        local_engine, local_session = connection(self.local_url)
        server_engine, server_session = connection(self.server_url)
        data = local_session.query(CerebrovascularDiseases).order_by(CerebrovascularDiseases.rank).all()
        print(len(data))
        if 'cerebrovascular' in server_engine.table_names():
            table = Table("cerebrovascular", Base.metadata, autoload=True)
            table.drop(server_engine)
        CerebrovascularDiseases.metadata.create_all(server_engine)
        for i in data:
            server_session.add(
                CerebrovascularDiseases(rank=i.rank, nctNumber=i.nctNumber, title=i.title, acronym=i.acronym, status=i.status, studyResults=i.studyResults, conditions=i.conditions,
                                        interventions=i.interventions, outcomeMeasures=i.outcomeMeasures, sponsorCollaborators=i.sponsorCollaborators, gender=i.gender, age=i.age,
                                        phases=i.phases, enrollment=i.enrollment, fundedBys=i.fundedBys, studyType=i.studyType, studyDesigns=i.studyDesigns, otherIDs=i.otherIDs,
                                        startDate=i.startDate, primaryCompletionDate=i.primaryCompletionDate, completionDate=i.completionDate, firstPosted=i.firstPosted,
                                        resultsFirstPosted=i.resultsFirstPosted, lastUpdatePosted=i.lastUpdatePosted, locations=i.locations, studyDocuments=i.studyDocuments, url=i.url,
                                        studyDescription=i.studyDescription, studyDesign=i.studyDesign, armsandInterventions=i.armsandInterventions, outcomeMeasuresII=i.outcomeMeasuresII,
                                        groupsandCohorts=i.groupsandCohorts, eligibilityCriteria=i.eligibilityCriteria, contactsandLocaons=i.contactsandLocaons,
                                        moreInformation=i.moreInformation))
            server_session.commit()
            print(f'success! {i.rank}')


if __name__ == '__main__':
    lts = LocalToServer(SQLALCHEMY_DATABASE_URI, BIT_URI)
    lts.go()
