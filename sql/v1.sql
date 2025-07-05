CREATE TABLE Activities (
    activityId SERIAL PRIMARY KEY,
    activityName VARCHAR(255) NOT NULL UNIQUE,
    autoCheck BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE Patients (
    patientId SERIAL PRIMARY KEY,
    pFirstName VARCHAR(50) NOT NULL,
    pLastName VARCHAR(50) NOT NULL,
    pBirthday DATE NOT NULL CHECK (pBirthday <= CURRENT_DATE),
    pUsername VARCHAR(30) NOT NULL UNIQUE,
    pPassword VARCHAR(72) NOT NULL -- bcrypt hashed password
);

CREATE TABLE SLP (
    slpId SERIAL PRIMARY KEY,
    slpFirstName VARCHAR(50) NOT NULL,
    slpLastName VARCHAR(50) NOT NULL,
    slpUsername VARCHAR(30) NOT NULL UNIQUE,
    slpPassword VARCHAR(72) NOT NULL -- bcrypt hashed password
);

CREATE TABLE Assignments (
    assignmentId SERIAL PRIMARY KEY,
    patientId INTEGER NOT NULL REFERENCES Patients(patientId) ON DELETE CASCADE,
    slpId INTEGER NOT NULL REFERENCES SLP(slpId) ON DELETE CASCADE,
    daysRequired INTEGER,
    aStartDate DATE NOT NULL DEFAULT CURRENT_DATE,
    aEndDate DATE NOT NULL CHECK (aEndDate >= aStartDate)
);

CREATE TABLE Templates (
    templateId SERIAL PRIMARY KEY,
    activityId INTEGER NOT NULL REFERENCES Activities(activityId) ON DELETE CASCADE,
    templateName VARCHAR(100) NOT NULL,
    templateLevel SMALLINT NOT NULL CHECK (templateLevel BETWEEN 1 AND 10)
);

CREATE TABLE AssignmentHistories (
    ahId SERIAL PRIMARY KEY,
    assignmentId INTEGER NOT NULL REFERENCES Assignments(assignmentId) ON DELETE CASCADE,
    templateId INTEGER NOT NULL REFERENCES Templates(templateId) ON DELETE RESTRICT,
    retries SMALLINT NOT NULL DEFAULT 0 CHECK (retries >= 0)
);

CREATE TABLE TemplateContents (
    tcId SERIAL PRIMARY KEY,
    templateId INTEGER NOT NULL REFERENCES Templates(templateId) ON DELETE CASCADE,
    sentence TEXT,
    imageURL VARCHAR(255),
    audioURL VARCHAR(255)
);
