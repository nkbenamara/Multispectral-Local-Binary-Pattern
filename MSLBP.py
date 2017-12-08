
def thresholded(center, pixels):
    out = []
    for a in pixels:
        if a >= center:
            out.append(1)
        else:
            out.append(0)
    return out

def intensity_or_corner(image, x, y, default=0):
    try:
        return image[x,y]
    except IndexError:
        return default

def MSLBP(img1,img2):

    mslbp_img0 = np.zeros_like(img1)
    mslbp_img1 = np.zeros_like(img2)
    mslbp_img = np.zeros_like(img2)


    for x in range(0, len(img1)):
        for y in range(0, len(img1[0])):
            center1 = img1[x, y]
            center2 = img2[x, y]

            top_left1 = intensity_or_corner(img1, x - 1, y - 1)
            top_left2 = intensity_or_corner(img2, x - 1, y - 1)

            top_up1 = intensity_or_corner(img1, x, y - 1)
            top_up2 = intensity_or_corner(img2, x, y - 1)

            top_right1 = intensity_or_corner(img1, x + 1, y - 1)
            top_right2 = intensity_or_corner(img2, x + 1, y - 1)

            right1 = intensity_or_corner(img1, x + 1, y)
            right2 = intensity_or_corner(img2, x + 1, y)

            left1 = intensity_or_corner(img1, x - 1, y)
            left2 = intensity_or_corner(img2, x - 1, y)

            bottom_left1 = intensity_or_corner(img1, x - 1, y + 1)
            bottom_left2 = intensity_or_corner(img2, x - 1, y + 1)

            bottom_right1 = intensity_or_corner(img1, x + 1, y + 1)
            bottom_right2 = intensity_or_corner(img2, x + 1, y + 1)

            bottom_down1 = intensity_or_corner(img1, x, y + 1)
            bottom_down2 = intensity_or_corner(img2, x, y + 1)

            values1 = thresholded(center1, [top_left1, top_up1, top_right1, right1, bottom_right1,bottom_down1, bottom_left1, left1])

            values2= thresholded(center2, [top_left2, top_up2, top_right2, right2, bottom_right2,bottom_down2, bottom_left2, left2])

            values12 = thresholded(center1, [top_left2, top_up2, top_right2, right2, bottom_right2,bottom_down2, bottom_left2, left2])

            values21 = thresholded(center2, [top_left1, top_up1, top_right1, right1, bottom_right1,bottom_down1, bottom_left1, left1])

            weights = [128, 64, 32, 16, 8, 4, 2, 1]
            values_mslbp1=[]
            values_mslbp0=[]

            for i in range(0,8):
                t=values1[i] + values2[i] + values12[i] + values21[i]
                if t>1:
                    values_mslbp1.append(1)
                    if t>2:
                        values_mslbp0.append(1)
                if t<=1:
                    values_mslbp1.append(0)
                    values_mslbp0.append(0)

            res0 = 0
            res1=0
            res_mean=0
            for a in range(0, len(values_mslbp0)):
                res0 += weights[a] * values_mslbp0[a]
                res1 += weights[a] * values_mslbp1[a]
                res_mean=int((res0+res1)/2)
            mslbp_img0.itemset((x, y), res0)
            mslbp_img1.itemset((x, y), res1)
            mslbp_img.itemset((x,y),res_mean)

        bins=[]
        for i in range(0,256):
            bins.append(i)
        mslbp_hist=np.histogram(mslbp_img,bins)[0]
    return mslbp_img,mslbp_hist



