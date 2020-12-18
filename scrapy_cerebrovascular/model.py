from sqlalchemy import Column, String, Integer, JSON, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class CerebrovascularDiseases(Base):
    """
    rank,nctNumber,title,acronym,status,studyResults,conditions,interventions,outcomeMeasures
    sponsorCollaborators,gender,age,phases,enrollment,fundedBys,studyType,studyDesigns,otherIDs,
    startDate,primaryCompletionDate,completionDate,firstPosted,resultsFirstPosted,lastUpdatePosted
    locations,studyDocuments,url
    """
    __tablename__ = 'cerebrovascular'

    rank = Column(Integer, primary_key=True, autoincrement=True)
    nctNumber = Column(String(200), unique=True)
    title = Column(Text)
    acronym = Column(String(200))
    status = Column(String(200))
    studyResults = Column(String(200))
    conditions = Column(Text)
    interventions = Column(Text)
    outcomeMeasures = Column(Text)
    sponsorCollaborators = Column(Text)
    gender = Column(String(200))
    age = Column(String(200))
    phases = Column(String(200))
    enrollment = Column(Integer)
    fundedBys = Column(String(200))
    studyType = Column(String(200))
    studyDesigns = Column(String(200))
    otherIDs = Column(Text)
    startDate = Column(String(200))
    primaryCompletionDate = Column(String(200))
    completionDate = Column(String(200))
    firstPosted = Column(String(200))
    resultsFirstPosted = Column(String(200))
    lastUpdatePosted = Column(String(200))
    locations = Column(Text)
    studyDocuments = Column(Text)
    url = Column(String(200))
    studyDescription = Column(Text)
    studyDesign = Column(Text)
    armsandInterventions = Column(Text)
    outcomeMeasuresII = Column(Text)
    groupsandCohorts = Column(Text)
    eligibilityCriteria = Column(Text)
    contactsandLocaons = Column(Text)
    moreInformation = Column(Text)


class CDtoC(Base):
    """
    rank,nctNumber,title,acronym,status,studyResults,conditions,interventions,outcomeMeasures
    sponsorCollaborators,gender,age,phases,enrollment,fundedBys,studyType,studyDesigns,otherIDs,
    startDate,primaryCompletionDate,completionDate,firstPosted,resultsFirstPosted,lastUpdatePosted
    locations,studyDocuments,url
    """
    __tablename__ = 'cerebrovascularc'

    rank = Column(Integer, primary_key=True, autoincrement=True)
    nctNumber = Column(String(200), unique=True)
    title = Column(Text)
    acronym = Column(String(200))
    status = Column(String(200))
    studyResults = Column(String(200))
    conditions = Column(Text)
    interventions = Column(Text)
    outcomeMeasures = Column(Text)
    sponsorCollaborators = Column(Text)
    gender = Column(String(200))
    age = Column(String(200))
    phases = Column(String(200))
    enrollment = Column(Integer)
    fundedBys = Column(String(200))
    studyType = Column(String(200))
    studyDesigns = Column(String(200))
    otherIDs = Column(Text)
    startDate = Column(String(200))
    primaryCompletionDate = Column(String(200))
    completionDate = Column(String(200))
    firstPosted = Column(String(200))
    resultsFirstPosted = Column(String(200))
    lastUpdatePosted = Column(String(200))
    locations = Column(Text)
    studyDocuments = Column(Text)
    url = Column(String(200))
    studyDescription = Column(Text)
    studyDesign = Column(Text)
    armsandInterventions = Column(Text)
    outcomeMeasuresII = Column(Text)
    groupsandCohorts = Column(Text)
    eligibilityCriteria = Column(Text)
    contactsandLocaons = Column(Text)
    moreInformation = Column(Text)
