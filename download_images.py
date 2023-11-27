from simple_image_download import simple_image_download as simp


response = simp.simple_image_download

kewords = [
    "classroom cctv phootage",
    "students in classroom",
    "large number of people in classroom",
]

for keyword in kewords:
    response().download(keyword, 50)
