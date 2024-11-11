CREATE TABLE "users" (
  "user_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "name" varchar(50) NOT NULL,
  "username" varchar(20) UNIQUE NOT NULL,
  "email" varchar(50) UNIQUE NOT NULL,
  "password" varchar(100) NOT NULL,
  "reset_code" varchar(100) NOT NULL,
  "rollno" varchar(20) UNIQUE NOT NULL,
  "dual_degree" boolean NOT NULL,
  "side_work" boolean NOT NULL,
  "additional_education" varchar(100),
  "verified" boolean NOT NULL
);

CREATE TABLE "courses" (
  "course_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "code" varchar(20) NOT NULL,
  "name" varchar(100) NOT NULL,
  "duration" varchar(10) NOT NULL,
  "level" varchar(30) NOT NULL,
  "description" text NOT NULL,
  "professor" varchar(50) NOT NULL,
  "course_type" varchar(20) NOT NULL,
  "is_active" boolean NOT NULL
);

CREATE TABLE "reviews" (
  "review_id" integer PRIMARY KEY,
  "review" text,
  "difficulty" integer NOT NULL,
  "rating" integer NOT NULL,
  "support" integer NOT NULL,
  "user_id" integer NOT NULL,
  "course_id" integer NOT NULL
);

CREATE TABLE "enrollments" (
  "enrollment_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "course_id" integer NOT NULL,
  "user_id" integer NOT NULL,
  "marks" integer NOT NULL,
  "term" varchar(10) NOT NULL,
  "year" integer NOT NULL,
  "study_hours" integer NOT NULL
);

ALTER TABLE "reviews" ADD FOREIGN KEY ("course_id") REFERENCES "courses" ("course_id");

ALTER TABLE "reviews" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "enrollments" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "enrollments" ADD FOREIGN KEY ("course_id") REFERENCES "courses" ("course_id");
