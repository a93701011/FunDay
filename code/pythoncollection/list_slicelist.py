favorite_things = ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles',
                   'warm woolen mittens', 'bright paper packages tied up with string',
                   'cream colored ponies', 'crisp apple strudels']
slice1 = favorite_things[1:4]
slice2 = favorite_things[6:8]
#slice list or string can be slice
list =[1,2,3,4,5,6,7,8,9,10]
list[::2] #[start:stop:step] return even index
list[::-1] # reverse the order
#list can be mutable
#del
#replace
color_list=["pink","yello","purple","indigo","green","black"]
del color_list[2:6]
color_list[0:1]=["green"]
color_list[0:2]=["green","white"]
color_list[0:1]="white"
color_list[0:5]=["".join(color_list[0:5])]

