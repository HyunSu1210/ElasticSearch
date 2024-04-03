### 파이널 프로젝트 (hope) elasticsearch에 데이터 적재하기 위해 데이터 가공 / 정제한 과정입니다.
- 공공 데이터 포털의 api를 활용
- python, flask, pandas 이용

의약품 검색 기능을 만들기 위해 elasticsearch를 사용했고 해당 프로젝트는 elasticsearch에 데이터 인덱싱을 하기 위해 가공 / 정제한 과정입니다.
<br />
데이터셋은 공공 데이터 포털의 api를 활용해 구하고 원하는 형식으로 사용하기 위해 가공 과정을 거쳤습니다.
<br />
데이터셋의 특이한 점은 첫번째로, JSON 형식이지만 XML 태그가 포함되어 있었습니다. html에서 데이터를 표시했을 때 XML 태그가 그대로 표현되었기 때문에 제거하는 과정을 거쳤고,
두번째로, 의약품 설명이 링크로 되어 있어서 변환이 필요했습니다. 해당 링크를 클릭하면 파일이 다운로드 되어 정보를 표시할 때마다 크롤링하여 사용해야 하는 번거로움이 있기 때문에 새로운 데이터셋을 구해 가공하고 병합하는 과정을 거쳤습니다.
<br />
이후 데이터셋의 결측치 제거하고 elasticsearch에 인덱싱하는 과정이 담겨있습니다.

