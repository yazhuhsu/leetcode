import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    def verify(data):
        if data['x'] + data['y'] > data['z'] and \
            data['x'] + data['z'] > data['y'] and \
            data['y'] + data['z'] > data['x']:
            return 'Yes'
        else:
            return 'No'

    triangle['triangle'] = triangle.apply(lambda x: verify(x), axis=1)

    return triangle

triangle = {
    'x': [13, 10],
    'y': [15, 20],
    'z': [30, 15]
}

output = triangle_judgement(pd.DataFrame(data=triangle))
print(output)