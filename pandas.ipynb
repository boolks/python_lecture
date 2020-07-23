import pandas as pd

data = pd.read_csv('data/data_draw_korea.csv')
print(type(data))
data.head()
data.tail()

# head, tail 함수의 default 값은 5

# column 명
print(data.columns)
# index
print(data.index)
# 몇 행 몇 열
print(data.shape)
# info() - Dataframe의 meta 정보
data.info()
# describe() - 집계함수
data.describe()

print(type(data['인구수']))
data['인구수'].head()
print('최소', data['인구수'].min())
print('평균', data['인구수'].mean())
print('최대', data['인구수'].max())

# 컬럼명 변경
data = data.rename(columns={'Unnamed: 0':'seq'})
data.head(2)

# seq 컬럼을 index로 변경하기
data = data.set_index('seq')
data.head(2)

# 컬럼의 특정 구간을 주려면 : 를 사용한다.
# 인구수, 행정구역 광역시도 3개의 컬럼 선택
data.loc[:,['인구수', '광역시도', '행정구역']].head(3)

data.loc[:,'인구수':'면적'].head(3)
# 1개 행만 선택
data.loc[0,:]
# 여러개의 특정행
data.loc[[0, 3, 4],:]

# 전국 데이터 중에 가장 높은 인구수
# data_loc['인구수'].max()
# 강원도에서 가장 높은 인구수는?
data.loc[data['광역시도'] == '강원도', '인구수'].max()

def get_pop_max(city):
    return data.loc[data['광역시도'] == city, '인구수'].max()

def get_pop_max_df(city):
    return data.loc[data['인구수'] == get_pop_max(city), ['광역시도', '행정구역', '인구수']]

# 새로운 DataFrame 생성하기
max_pop_df = pd.DataFrame(columns=['광역시도', '행정구역', '인구수'])
for city in data['광역시도'].unique():
    max_pop_df = max_pop_df.append(get_pop_max_df(city))
max_pop_df

# reset_index(drop=False) - 인덱스 조정
# 인덱스를 변경하면서 기존 인덱스 값을 컬럼으로 변경
# drop = True 로 설정하면 기존 인덱스 값이 포함된 index 컬럼을 drop
max_pop_df = max_pop_df.reset_index(drop = True)
