from sqlalchemy import Table
from sqlalchemy.exc import IntegrityError

from scrapy_cerebrovascular.model import Base, CerebrovascularDiseases
from util.pg_connection import connection
from util.csv_operation import read_csv


class LoadToDB:
    def __init__(self):
        self.session, engine, metadata, tables = connection()
        if "cerebrovascular" not in engine.table_names():
            Base.metadata.create_all(engine)
        else:
            table = Table("cerebrovascular", metadata, autoload=True)
            try:
                table.drop(engine)
            except IntegrityError:
                print("Fail to delete data tables.")
            Base.metadata.create_all(engine)

    def process_item(self, results):
        if results:
            for result in results:
                data = CerebrovascularDiseases(nctNumber=result[1],
                                               title=result[2],
                                               acronym=result[3],
                                               status=result[4],
                                               studyResults=result[5],
                                               conditions=result[6],
                                               interventions=result[7],
                                               outcomeMeasures=result[8],
                                               sponsorCollaborators=result[9],
                                               gender=result[10],
                                               age=result[11],
                                               phases=result[12],
                                               fundedBys=result[14],
                                               studyType=result[15],
                                               studyDesigns=result[16],
                                               otherIDs=result[17],
                                               startDate=result[18],
                                               primaryCompletionDate=result[19],
                                               completionDate=result[20],
                                               firstPosted=result[21],
                                               resultsFirstPosted=result[22],
                                               lastUpdatePosted=result[23],
                                               locations=result[24],
                                               studyDocuments=result[25],
                                               url=result[26])
                if result[13]:
                    data.enrollment = int(result[13])

                try:
                    self.session.add(data)
                    self.session.commit()
                except:
                    print(f"{result[0]} : failure ！")
                    self.session.rollback()


if __name__ == '__main__':
    results = read_csv('sr.csv')
    ltdb = LoadToDB()
    ltdb.process_item(results)
    print("load to pg success !")
