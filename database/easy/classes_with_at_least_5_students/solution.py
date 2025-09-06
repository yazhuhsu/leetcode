import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # step1.
    # courses.groupby('class').describe())
    #          student                
    #            count unique top freq
    # class                           
    # Biology        1      1   D    1
    # Computer       1      1   F    1
    # English        1      1   B    1
    # Math           6      6   A    1
    # =======================================
    # step2.
    # courses.groupby('class')['class'].count()
    # class
    # Biology     1
    # Computer    1
    # English     1
    # Math        6
    # Name: class, dtype: int64
    # =======================================
    # step3.
    # courses.groupby('class')['class'].count().reset_index(name='count')
    #       class  count
    # 0   Biology      1
    # 1  Computer      1
    # 2   English      1
    # 3      Math      6

    classes = courses.groupby('class')['class'].count().reset_index(name='count')

    return pd.DataFrame(classes.loc[classes['count']>=5, 'class'])

data = {
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'class': ['Math', 'English', 'Math', 'Biology', 'Math', 'Computer', 'Math', 'Math', 'Math']
}
print(find_classes(pd.DataFrame(data=data)))