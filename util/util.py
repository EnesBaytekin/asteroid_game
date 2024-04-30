def collide_rect(rectA, rectB):
    Ax, Ay, Aw, Ah = rectA
    Bx, By, Bw, Bh = rectB
    return (
        Ax <= Bx+Bw and
        Bx <= Ax+Aw and
        Ay <= By+Bh and
        By <= Ay+Ah
    )

def is_inside(rect_inner, rect_outer):
    ix, iy, iw, ih = rect_inner
    ox, oy, ow, oh = rect_outer
    return (
        ox    < ix and
        ix+iw < ox+ow and
        oy    < iy and
        iy+ih < oy+oh
    )