from sqlalchemy import func, desc, and_


def select_1(session, Student, Score):
    return session.query(Student.name, func.avg(Score.score).label('avg_score')) \
        .select_from(Score) \
        .join(Student) \
        .group_by(Student.id) \
        .order_by(desc('avg_score')) \
        .limit(5) \
        .all()


def select_2(session, Student, Score, Lesson):
    return session.query(Student.name, func.avg(Score.score).label('avg_score')) \
        .select_from(Score) \
        .join(Student) \
        .join(Lesson) \
        .where(Lesson.id == 1) \
        .group_by(Student.id) \
        .order_by(desc('avg_score')) \
        .first()
        

def select_3(session, Student, Score, Lesson, Groupe):
    return session.query(Groupe.name, func.avg(Score.score).label('avg_score')) \
        .select_from(Groupe) \
        .join(Student) \
        .join(Score) \
        .join(Lesson) \
        .where(Lesson.id == 1) \
        .group_by(Groupe.name) \
        .all()
        

def select_4(session, Score):
    return session.query(func.avg(Score.score).label('avg_score')).one()


def select_5(session, Lesson, Teacher):
    return session.query(Lesson.lesson) \
        .join(Teacher) \
        .where(Teacher.id == 2) \
        .all()


def select_6(session, Student, Groupe):
    return session.query(Student.name) \
        .join(Groupe) \
        .where(Groupe.id == 3) \
        .all()

def select_7(session, Student, Score, Lesson, Groupe):
    return session.query(Groupe.name, Student.name, Lesson.lesson, Score.score) \
        .select_from(Groupe) \
        .join(Student) \
        .join(Score) \
        .where(and_(Lesson.id == 8), (Groupe.id == 1)) \
        .all()

def select_8(session, Score, Lesson, Teacher):
    return session.query(Teacher.name, func.avg(Score.score).label('avg_score')) \
        .select_from(Teacher) \
        .join(Lesson) \
        .join(Score) \
        .where(Teacher.id == 4) \
        .group_by(Teacher.id) \
        .all()

def select_9(session, Student, Score, Lesson):
    return session.query(Lesson.lesson) \
        .select_from(Student) \
        .join(Score) \
        .join(Lesson) \
        .where(Student.id == 1) \
        .distinct() \
        .all()

def select_10(session, Student, Score, Lesson, Teacher):
    return session.query(Lesson.lesson) \
        .select_from(Teacher) \
        .join(Lesson) \
        .join(Score) \
        .join(Student) \
        .where(and_(Student.id == 1), (Teacher.id == 1)) \
        .distinct() \
        .all()