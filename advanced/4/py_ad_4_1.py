"""
    opensource prj
    장점
    1. 역량 향상 및 보유 스킬 능력 제시
    2. 인하우스와 달리 수 많은 디버깅, 개선을 통해 신뢰성 안정성 높은 어플리케이션 도출
    3. 적시에 사용가능
    4. 아키텍쳐 효용성, 고품질
    5. 문서, 개선가능성, 지적재산권 주의
    *사이드프로젝트(오픈소스) 참가 장점
    1. 답변, 기능추가, 사명감
    2. 이슈 해결을 통한 개발 역량 강화
    3. 코드퀄리티, 알고리즘, 다양한 지식 향상
    4. ** 구직시 합격 가능 매우 높음

"""
# jpg,png -> gif
import glob
from PIL import Image  # pip install image

path_in = "./project/images/*.png"
path_out = "./project/image_out/result.gif"

img, *images = [
    Image.open(f).resize((320, 240), Image.ANTIALIAS)
    for f in sorted(glob.glob(path_in))
]

print(img)
print(images)


img.save(
    fp=path_out, format="GIF", append_images=images, save_all=True, duration=500, loop=0
)
