CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES ('admin', 'admin');
SELECT * FROM users;

CREATE TABLE etudiant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT NOT NULL,
    matiere TEXT NOT NULL,
    note REAL NOT NULL CHECK(note >= 10 AND note <= 20) -- Constraint to ensure note is between 10 and 20
);

-- Insert sample data into the etudiant table
INSERT INTO etudiant (nom, prenom, email, matiere, note) VALUES 
('Doe', 'John', 'john.doe@example.com', 'Mathematics', 15.5),
('Smith', 'Jane', 'jane.smith@example.com', 'Physics', 19.0),
('Brown', 'Charlie', 'charlie.brown@example.com', 'Chemistry', 12.0),
('Taylor', 'Emily', 'emily.taylor@example.com', 'Biology', 18.0),
('Johnson', 'Michael', 'michael.johnson@example.com', 'History', 14.0);


INSERT INTO etudiant (nom, prenom, email, matiere, note) VALUES 
('Anderson', 'Laura', 'laura.anderson@example.com', 'Mathematics', 16.0),
('Wilson', 'James', 'james.wilson@example.com', 'Physics', 17.5),
('Martinez', 'Sophia', 'sophia.martinez@example.com', 'Chemistry', 13.0),
('Garcia', 'Daniel', 'daniel.garcia@example.com', 'Biology', 18.5),
('Lopez', 'Isabella', 'isabella.lopez@example.com', 'History', 14.5),
('Clark', 'Ethan', 'ethan.clark@example.com', 'Mathematics', 19.0),
('Rodriguez', 'Olivia', 'olivia.rodriguez@example.com', 'Physics', 15.0),
('Lewis', 'Mason', 'mason.lewis@example.com', 'Chemistry', 12.5),
('Walker', 'Emma', 'emma.walker@example.com', 'Biology', 17.0),
('Hall', 'Lucas', 'lucas.hall@example.com', 'History', 16.5);

SELECT * FROM etudiant;