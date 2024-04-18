import faker
import datetime
import sqlalchemy
import random

from sqlalchemy import create_engine, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, Mapped, mapped_column
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql://postgres:monica@localhost:5432/postgres')
DBSession = sessionmaker(bind=engine)

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    groupe_id: Mapped[int] = mapped_column(ForeignKey('groupes.id', ondelete="CASCADE"))


class Groupe(Base):
    __tablename__ = 'groupes'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


class Teacher(Base):
    __tablename__ = 'teachers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


class Lesson(Base):
    __tablename__ = 'lessons'

    id: Mapped[int] = mapped_column(primary_key=True)
    lesson: Mapped[str] = mapped_column(String, nullable=False)
    teacher_id : Mapped[int] = mapped_column(ForeignKey('teachers.id', ondelete="CASCADE"))


class Score(Base):
    __tablename__ = 'scores'

    id: Mapped[int] = mapped_column(primary_key=True)
    score: Mapped[float] = mapped_column(Float, nullable=False)
    date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id', ondelete="CASCADE"))
    lesson_id: Mapped[int] = mapped_column(ForeignKey('lessons.id', ondelete="CASCADE"))


def init_db():
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

    fake_data = faker.Faker()

    student_amount = 50
    groupe_amount = 3
    lesson_amount = 8
    teacher_amount = 5
    score_amount = 20

    with DBSession() as session:

        groupes = []

        for _ in range(groupe_amount):
            groupe = Groupe(name = fake_data.unique.company())
            groupes.append(groupe)
            session.add(groupe)

        session.commit()

        students = []

        for num in range(student_amount):
            student = Student(
                name = fake_data.unique.name(),
                groupe_id = groupes[num % groupe_amount - 1].id
            )
            students.append(student)
            session.add(student)
        
        session.commit()

        teachers = []

        for _ in range(teacher_amount):
            teacher = Teacher(name = fake_data.unique.name())
            teachers.append(teacher)
            session.add(teacher)
        
        session.commit()

        lessons = []

        for num in range(lesson_amount):
            lesson = Lesson(
                lesson = fake_data.unique.catch_phrase(),
                teacher_id = teachers[num % teacher_amount - 1].id
            )
            lessons.append(lesson)
            session.add(lesson)

        session.commit()

        for i in range(student_amount):
            for j in range(score_amount):
                score = Score(
                    score=random.uniform(1.0, 12.0),
                    date = fake_data.date_time(),
                    student_id = students[i].id,
                    lesson_id = lessons[j % lesson_amount - 1].id
                )
                session.add(score)

        session.commit()


from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10


def show_db():
    with DBSession() as session:
        result_1 = select_1(session, Student, Score)
        result_2 = select_2(session, Student, Score, Lesson)
        result_3 = select_3(session, Student, Score, Lesson, Groupe)
        result_4 = select_4(session, Score)
        result_5 = select_5(session, Lesson, Teacher)
        result_6 = select_6(session, Student, Groupe)
        result_7 = select_7(session, Student, Score, Lesson, Groupe)
        result_8 = select_8(session, Score, Lesson, Teacher)
        result_9 = select_9(session, Student, Score, Lesson)
        result_10 = select_10(session, Student, Score, Lesson, Teacher)
    
    print(f"SELECT 1\n{result_1}\n")
    print(f"SELECT 2\n{result_2}\n")
    print(f"SELECT 3\n{result_3}\n")
    print(f"SELECT 4\n{result_4}\n")
    print(f"SELECT 5\n{result_5}\n")
    print(f"SELECT 6\n{result_6}\n")
    print(f"SELECT 7\n{result_7}\n")
    print(f"SELECT 8\n{result_8}\n")
    print(f"SELECT 9\n{result_9}\n")
    print(f"SELECT 10\n{result_10}\n")


if __name__ == "__main__":
    # init_db()
    show_db()
