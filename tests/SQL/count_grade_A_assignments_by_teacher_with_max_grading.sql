-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH graded_assignments AS (
    SELECT
        teacher_id,
        COUNT(*) AS total_assignments
    FROM
        assignments
    WHERE
        grade IS NOT NULL
    GROUP BY
        teacher_id
),
top_teacher AS (
    SELECT
        teacher_id
    FROM
        graded_assignments
    ORDER BY
        total_assignments DESC
    LIMIT 1
)
SELECT
    COUNT(*) AS grade_A_count
FROM
    assignments
WHERE
    teacher_id = (SELECT teacher_id FROM top_teacher)
    AND grade = 'A';
