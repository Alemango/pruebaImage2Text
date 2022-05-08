import dropbox

file_from = './test.png'
file_to = '/test.png'

dbx = dropbox.Dropbox('sl.BHKX0xVBXem7TSVzgB8UGN1U7ezfZ2oZfws4yZAEFGvGox3TAyjxUKUB3_hhrDY_YBZzDhyH_zNM3NS2lBKXnjutI8I1xyinxDl7RE_8IB98-0_LAxCWZSJ1fHS5SFQCXYS-RRo')
dbx.files_upload(open(file_from, 'rb').read(), file_to)