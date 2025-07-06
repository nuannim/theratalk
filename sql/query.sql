CREATE View assignment_full AS

SELECT *
FROM Assignments a
INNER JOIN Patients p ON a.patientId = p.patientId
INNER JOIN SLP s ON a.slpId = s.slpId
INNER JOIN AssignmentHistories ah ON a.assignmentId = ah.assignmentId
INNER JOIN Templates t ON ah.templateId = t.templateId
INNER JOIN Activities act ON t.activityId = act.activityId
LEFT JOIN TemplateContents tc ON t.templateId = tc.templateId;


CREATE VIEW assignment_full AS
SELECT
    a.assignmentId AS assignment_id,
    a.patientId AS assignment_patient_id,
    a.slpId AS assignment_slp_id,
    a.daysRequired,
    a.aStartDate,
    a.aEndDate,
    p.patientId AS patient_id,
    p.pUsername,
    p.pFirstName,
    p.pLastName,
    s.slpId AS slp_id,
    s.slpUsername,
    ah.assignmentHistoryId,
    ah.assignmentId AS ah_assignment_id,
    ah.templateId AS ah_template_id,
    t.templateId AS template_id,
    t.templateName,
    act.activityId AS activity_id,
    act.activityName,
    tc.templateContentId,
    tc.sentence,
    tc.imageURL,
    tc.audioURL
FROM Assignments a
INNER JOIN Patients p ON a.patientId = p.patientId
INNER JOIN SLP s ON a.slpId = s.slpId
INNER JOIN AssignmentHistories ah ON a.assignmentId = ah.assignmentId
INNER JOIN Templates t ON ah.templateId = t.templateId
INNER JOIN Activities act ON t.activityId = act.activityId
LEFT JOIN TemplateContents tc ON t.templateId = tc.templateId;