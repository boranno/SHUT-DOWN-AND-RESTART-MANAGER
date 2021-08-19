from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import os
import base64
root=Tk()

bt_i=b'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'
abort_i=b'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'
bg_i=b'iVBORw0KGgoAAAANSUhEUgAAAaQAAAGQCAIAAABuxYPZAAAACXBIWXMAAA7zAAAO8wEcU5k6AAAAEXRFWHRUaXRsZQBQREYgQ3JlYXRvckFevCgAAAATdEVYdEF1dGhvcgBQREYgVG9vbHMgQUcbz3cwAAAALXpUWHREZXNjcmlwdGlvbgAACJnLKCkpsNLXLy8v1ytISdMtyc/PKdZLzs8FAG6fCPGXryy4AAAbk0lEQVR42u3dSXbkzG6GYSBUvvvz/mdegqeuBDyIDsEumUwyG9X7HJ/fKopiEyRRzLqfEPq///PfIqJuSbx+YSKiYu4uIi5JKnf/m/5Tlru7JhFRVREx17yOSSrfzauptHVENC+81ZWlbtzrH/t2VETUPH8neVJXEU9tm2V9tbI707bcRNsRqqqq5hVubkl+8rfyIbu7qYgkFxFRk6T645LcPR9b3uatno6ISFIRFRGTru46/Z9bOWD3dsD5xFV/LJxyWUf6yeShNpU2nvnYJGm8BP2/1parq5iIe/1CRVVdkpp6XT8fdjsqU3HXPPh1hXSrl0JVw/GL63B944n3Q/J2/MlFTfzm7po8qXiyfEHqdtoI16s/vSXyCP/V//SRD8vn3N0kSfqJQ9SPVlMfN01tmzcdjsTqdZGk4mU1U2mH4PJnctGtfJ1U1eqdb/lpUrW+kXBerimlm3i7b1zLflO/dSUPWhv2do/F0zdP2i+NthtDdbzE1naUJsPoKiLq9aEru64XNB92u8rii4fRHz11MXG3ciSqaprKA9gut/YHxr08j7fh+SrD5cPDla9XUk3u/tes3k6pVap2G88ezHEpAPxiFDsAFDsAoNgBAMUOACh2AECxA4Ar/DlrQy3sU0JTLU4lvrh+jFzFjWjPW7nEgN6OA8j7aok4VRWtqaW6dB7aWj6LtubsIO8fhtdAmUrOBLnLieMccmR6+g2hev42a3LrgY3X5NTeU2xDHEN28Yz88WMW9zbafaFuHkA4wRzwXNvx4qa21/fF+/MjTS70/FAPH7y7S4iCqmpL7/JmBwAUOwAUOwCg2AEAxQ4AKHYAQLEDgKv8KYmYWU5lMbqykZMK6/doW/2T7NzUgexYaKbmorKdilJVN08piYhZCS6pipm3RF47ru181jQ810/nj8gthA5vUrp3uYiJpPrfJK7yeFTOw/+JDvnDJHKrX5iL6Na2J5dnEih7dPzrFtoSlwvyehsOH//GBvPglCxXTYb6tJleGu6WegPXP/ZvhRVaQGwpfRbuunzXWHhArf6Q90CelaH2fGu5SBK1emW13G9qde1pO8LhZFxuLdT6xHC2x7+d++xxaf3sXljspGY+W+hWVADgt73ZmVmpcV7y6u77g+sA8CXFrr/Q1V+OcXHVj6t1tcu7j+/XvIcCeLDYafgdRgD4ZVJ7b2IsAPz+YqdjtwbGBcBv+xi7uHSj1cy78G92AM4vdi/4x7u1fnZmtZRp/HzttdOdtm/llVxOT1fJ8NFej+T+ZBrEqxkrldqBS57JtcUY17HjlBAl65P8+qvzcRvHtmd8XvPPLzvjnyU758NlGvsP8uHppRdu+WMsAPxuFDsAFDsAoNgBAMUOACh2AECxA4Ar/Pm0AwoRpGHe2LX2WjnHVMJrrYWBr6z5eChPXVwltYZidUnjNflXv7jVaWNVVFR+wjy2P15/C1nENaWNAFfLIaoOc+aO83EOP2LhC9cyZJ8Z6DorZnX1PKqt6d8z85zOg5BmNsyQvHQ6b7soOk7Cq4cuSpiv+ZnR480OACh2AECxA0CxAwCKHQBQ7ACAYgcAH+HynN08OuR1vtb5yu6T6Wd7P7vt+WdniZ635ZVaI7N8Ku527HjCxJpX9ZgrE7yO1+U1o3S3Xd2jyayPnVdg8T5PJWL5WSdSD9W1z6Gsx+6r1q4xp0Q/ZN5Y3uwA8DEWACh2AECxAwCKHQBQ7ACAYgcAB31TP7s2z2lLg31guKok7Prsrv2PX6Ed6nt7q+2cN3ay2rH+azvuRt95PHfHcz6H7OIe9+8rXqY2m/AHTnK/Niy82QEAxQ4AKHYAQLEDQLEDAIodAFDsAIBiF+fNrDaSRBvZrsVvvTcLNj/NMWEnkz++eJwfyvdpde5RDV35Hjydh1Zrc+x+4DM2uTdkvVXcF+Uxd95La7nCw/db/KnJqPJmBwAUOwAUOwCg2AEAxQ4AKHYAQLEDgKt80byxr4hQuXvbTwkKqYiIhQlWfTwQzd9I+ef0r1vPfGnpuHdifsr7QHmelbO0+VP5Ebl5+RvMPB/S3r5mNa/kmvTc8ZQ6Gn5li7VLE2qqenjzW/PG6q6V75y4xdxZOc64sLzQeIqP1dUP0d15Yw9frzjZcc3c7W01yJsdAD7GAgDFDgAodgBAsQMAih0AUOwA4KCesyvBnNByS0KbsLtJlp7r8eGPNmvolie1XGzppTmcFjbU5o212hlLJOa1QsO4MclVUnIyrCraz6Xm4HLqL/nkLFoU6MHoU45QtbMriaqPb1XWxtnP3qyHwZ+O7RPmjQJzuuvcHJnX++3w8faGa+FQzezRSF28n4c0auwOWbf5xr5+7UIvPEpL5eKVjwVvdgD4GPs9PmQeewAUOwB4pz/ffgLL7e2F9zsAvNkBoNgBAMUOAL7V6r/ZbcdkrrbY7esUk4BPnYVSWxpu0s/uFo8qB4hErH570tvOdRozXJrYtB/AgUZpmhuTuYu7qIVRSqb5rJKVvnTqknSMK55+KVV+ahjtllN6Oa5p8lcklX9BLcOU/2Ytg7d9JGW4RERNW2dDTzVQFnOdZUBURFWuv1PT2gGH+JvXYzaRn3ayLX25NT9y7d/oKjk4miOgJuJavr6FPKSL90law+MTjqfvcT7mfclJMYbWuPDRoO7e0U+pNcure/Gd2+fNDgAfYwGAYgcAFDsAoNgBAMUOACh2AHDQ6+aNjUGYE3M3Fx2tHO1n91uFQNby8pgmk3t95e5efQ+NCyd3jojMp6C9e0fFZFYMgvnCHv2ioZs8C3H3bb+P/lr3Rj+7HL/bnrn4ij6Gubmk9NmNP6WZI292APgYCwAUOwCg2AEAxQ4AKHYAQLEDgINWc3Y9lzSJHZ0UO6vBKBeRlFLYqa6tL7XFmQyT0A6JntebTGBaj6d+qwyj5k557ZTbwocHVK1cFvHSyi2PiNacVmH169P6lNX7YfE6TtJk6uI7rv6Du66jmpu4Ld6uectx+/UCJWkd5eo6+QG4hZCainjuBKfDyab61a2M//R1IQyChr6Bq4OfUnIJVz80VXz09vuofnb1YezPhX9MrpY3OwB8jAUAih0AUOwAgGIHABQ7AKDYAcBBe+aNvSS9VoNONSVXdpo+ss3dlnngq6Xnwgnumjd27LD2HX30Lupn1+eNHVaubdqW1o9xv3kLPFvpZ6cnzpdab+kW4ts4zcVYqD4+8S397HizAwCKHQCKHQBQ7ACAYgcAFDsAoNgBwOVe188upurk8X52B3ZXI285cKSew32bP5W7zoUDPnaaC/3s9v9s3u1qMin3sMtbHnqrJdH8Y6n+NaYi6cAsqJMxan+0pRVa2zT30l9PVUTScCXVxFPYwAMNztQnk6uWhf2odPrdzesy7Wd3myXb8h7zf/Mxmva97Hg/iC0LffN4FrrLPTpvrMtf1aQq4snL7ZHPLnkMKKYWLUyLj/m39LPLJSJnLeeZSt7sAIBiB4BiBwAUOwCg2AEAxQ4AKHYAcIkP7We3mEJ6dPsyTDla4jnbW43ZukmPsEf3W+fufPhnt/vZxfzg8MeL29+Fa7RwzPVI2pI7ecm72ag+FLr3+oZZUtdPoa6Tx83MPOls8F/RfK1dsif32/vZua/0s1sOo5UBTCf3s2vnNXmUFm/RY+G7ds+3OXN3boc3OwB8jAUAih0AUOwAgGIHABQ7AKDYAcBBf67ewVLebV/MSp/d77wh3Qv62UkPmvWN7IwT7elnN3YDHLqGXUpXhkPlpybFbjmtVQ/fak+92oOv/M1qDwyFiMdkZGtsp9L6vqU60i5i6zHKOG5t6GJKK8xUqy+Y59THUOUTG/oZbpfc4tCTiNVUYcqXafJYTabTPbGfXRxwaWO6dIs+GkSVWZ/KuJA3OwCg2AGg2AEAxQ4AKHYAQLEDAIodAFzl8pzdJJ4VGr35K/fbF17cz+4Z39/PrkX/TohJyksay/X5kV/bz+4Faj+74TRXbvjTcpqqKlrukhfEFXmzAwCKHQCKHQBQ7ACAYgcAFDsAoNgBwCus5ux6/mgSOzqan5qEbmosy0UkpRTW0a8e0NjArszmKZJbpNVJPNs46OR8P6SfnYa2cf2Pqj8iImKTUFbq7eFy3zrVvDScmVrusDa7+g8NaeiEuD4D6TzIWYcoSetyWNfJD8AtBCpVxHN0MV+Ffpbli9vmPLaTnW69ZaTkcXZdlWN99FpXvni0bQTaYLUxjG83JiJWWzzm9nYq4tLP3Q8+6e7DnfmCXC1vdgBAsQNAsQMAih0AUOwAgGIHABQ7ALjQas4udHZ7KvjW4jaq2pJEuQVbXiJDr7RUM086Cfm0NJcM33APM7T6B3Qiq83mWripxO5qhk7beOaFz8ybKa/tZ3fG7fDcrltebHahJ8HD+Y9YSMDlH5/MPfo8VU0LV2f9pLSf3RV99Pb2s8sRvy8pWO6eI5PSa8jexnm82QHgYywAUOwAgGIHABQ7AKDYAQDFDgAOenzeWPVpKsiTSArxq5yUs/yFjvX0ZfPGfqZJP7ul796ZN7YMrFodeS1ZwzIlbvspq1m/ZGZSmgaWFFg6b/znmbJ6jufk1zQMWGgEWHquSW7BNn73IX9llndz17rffEamfS93xkGH7oQb8xT7STPjarISX/UkqvmWyC0FZ89jvi3ScMBpOLHkcmuhu5c8oBZ2VfonilgYtrzQzribeLMDwMdYAKDYAQDFDgAodgBAsQMAih0AHLQ1b+y81deB5l+TrmHzdmNPag2tXtDT7aSj7f3sFs9le97YA+M/6fl1bshxbCTXe/b9azHKnKrz2Z1/df+/MG+sjvPG7ntweLMDAIodAPyij7Gf+AFQ64eC8Ds5Ls5VBMCbHQBQ7ABQ7ACAYgcAX2bPvLFdyVLVGTjrqiZioW7mnFiqUbEj/wPC86G5xZygu2s4wTB/KP8rx/Fx7uN5QT+7q7WcYAk5irTZjX/32427m4iKerhQpiK1V+DhdnuqKmP69UPGkzc7AHyMBQCKHQBQ7ACAYgcAFDsAoNgBwEFb/eykd1h7dfJIVZ/Mvi3mBOM8ni3KV/uvvT8KtGve2F/hc4Js7UjC4H9TyK43K3Rvs9Ye6DvJmx0AUOwAgGIHABQ7AKDYAQDFDgAodgCwamvCnclkr/JP5nfy3wa3fPp1ItC80MJUna5hhaOumDdWVc1MRFJKOU7o7um84OSxeWPvJjdDd7ll8/mIywZ1a4+TnzKzH1HLW5DhUvaebvk2qF/d9KkhasHVeqGn4xD36zVsmtvMae00195Q7PF5Y20cYh9XSy63tqGjN0ge5jbUvnm5U93VLT5fLlbHIZ/1M+PPmx0APsYCAMUOACh2AECxAwCKHQBQ7ADgWX8+87CenzcWbSR7yzMReUd3witMIp89cLdxR41pu8WZhcGbHQBQ7ACAYgcAFDsAoNgBAMUOACh2ADD1oTm7/fPGDvGxC2b8tLiv3LQuLJy0A/PnZru9Yt7Yq/vZjfG9tsS3j//u3vtQXJyE6/3R2rh7/a+XroKmpb3a/TMKwb3SZs4X2kFuRPxaLzlXaTd0crFws9n0STkyb+z8gN8iNhPsz5dO2wu28Z+06st33c7IJG92APgYCwB8jH2x9js+MnxS5LfKAPBmBwAUOwAUOwD4bfg3OwD/drFbzK28sc2cqkqbSjSEma7I1r3LFfPG5giSu5tZm9f17f3srjuGvOW4/fqFbh9JmKn2yLHNmwZKmEt3/S/vc67v/nljpwf8nc/IUJFEd/Yl5GMsgH8CxQ4AxQ4AKHYAQLEDAIodAFDsAOAKqzm7xRZRB+bZnM/vOYlBre19kk9aCxVrWtgUU4KuXIXz023tUrZMWcl8vSnBFQ5mOPe145nE8XJHvsNDoeMBfPJNeF0/O1WVGjPMD/KHzFP855se198eKgbAx1gAoNgBAMUOAIR/swPAmx0AUOwA4HcUu9V+dg8qWZtxC3e381BAadJKTNbbpX1I3uc3WZwUlXFevJnnY3XWxidjTsiUNzsAFDsAoNgBAMUOACh2AECxAwCKHQCc6cx+dm2CzqFH2BvnmV1a6OaTY95uYZb/NriVE8v/ryy0MFWna1jhX3JRP7swi+u1flxMhjsgX8ry33Yb1K9uetq45VOcZBLjfl3LV6YiLurlu+0Nxa6fN9bDdny8JEnK0E3u/Jz5ax39fHOa4FS3fIvPl4vVcchn3cb/rwynpqp5X3uihbzZAeBjLABQ7ACAYgcAFDsAoNgBAMUOAD6g2GnLDo1fxAhMW769qesaok0OaX6EH+Ks3mc54hTSWHdCSV4dPs49P75nhe3tzPskbq8fmx62i/6avnuLQ3Ti/SyH+tl9advByak9ND8vb3YAeLMDAIodAFDsAIBiBwAUOwCg2AHAQX+u3sEkCLNz3tjPYfFcctO6sNDHfE9rQPa8YcSeiNq1VF1Me93No13t+Yzb5Dj7cN27D1u+LI9M709XfzJ3VVMXcfHaTs50130uY6RUVcWHln8tZ1oP4oTn69J+dnmj7c4X7/f8/NGQx1s6xmaC/fnSaXtBO+Ou5M0OAB9jAYBiBwAUOwCg2AEAxQ4AKHYAcNBqzm4xb3VgHth5Hiong7ZjVqrnJdY+ibuH89Kl7/a816k7LaOqqi5f2chs//02ucHadMZX71dmrevyXLqL/ezW5o09vt+Qx/zA/oy82QEAxQ4AKHYAQLEDAIodAIodAFDsAOCL/fmtJ7Y4O6q7vzeAlPuO1YNZ/G4JS62mrzyJewnjqUkJJLrIj2j+sVT/GlORJDKMQ05KvmzK1LdcdxkbJtYk2uoViS0Xc0e1Y4OTk3PxAPbk3co6deelH5yLq2i9zsnFZKWR3NF+dtfe5HE2W/2U/pW82QHgYywAUOwAgGIHABQ7AKDYAQDFDgAO+tB5Yw80zptYjDjleTyByf0pQzNBP76dpXlj19aPzQvbfvXB+/5wP7v5AU+eu5gJ5c0OACh2AECxAwCKHQCc72saAdR/0I3/qisiLkwtAoA3OwCg2AHgY+xKPzhVFfVpGsmTSIpdq9xd1OqSI/V0/7yxcVJO3/Ejk4hfnULVt/82uOVd1AlI80ILLcRcwwqXUhNxUasjr6W9XYl0tUtm9WsVkV88UezTD4DeQuJMRVzVa+PDNmqpfnXT1TtWdbj+x+arjfv1+hCYiriol++mcI0P97MrAb31567McXxxY7x8Li5yi8+Xi9VxyGfdxt+SljZ5IU64sz8jb3YA+BgLABQ7AKDYAQDFDgAodgBAsQOAg878dTGtM57miSNrUk8n6+Tl27mY5/vZ3TnIOpFoiSjJR8yjGlucubdpZJ9K76mqmYlISklEzczd0/r4x9zi1Wd69zLpvS3EPom1QdvqBuf5rDwyk8H3l7Q8POvGO9zP7tKL694vkMuZ8xS7u2pqu+mnz5sdAFDsAFDsAIBiBwAUOwCg2AEAxQ4ArvN4zs7bVJg126ImYqFu5rRdqi3Uj8wbO6eaZ9TUtoe6uARtLorm2Xjqeec2LhlWOCmkNYxYnI3Ux7b0WnuB1a+trpZHa55F2g49vSaitStoKWODvs3j7MO1ucGYtssj0/vTeRjhOs5e28nZvVHZmDe2nWy7Fu/NwX0UC2Pfn68w3W5eaGcMGG92APgYCwAUOwCg2AEAxQ4AKHYAQLEDgKPFLsaO4heLUaBj+Tgdw0eyI2f0riBSPMHJkeOicT4mhgfblfrM6XHnLQI/pHnidYeh1ennu9iXcOdzypsdAD7GAgDFDgAodgBAsQMAih0AUOwA4KA/w2Sv8Qvxf3A4YmBn3qHsE5R2grH5msuPi6iYi7gkFctdwFRcTmvxd7dh3KNb2529Skv71N6fTq3G2FwlPXp4f0Rv4UKriOcklw4n27Z7W++vN5nht56gro9nCIu9avLiFI7ARMSHnoymfYl/ZA1g3lgAoNgBAMUOAMUOACh2AECxAwCKHQC8wZ/PPKznJ4FdbMlX41MiOaIlbRJbDz/VV3jxWddmf/lI3jfyTGx6PTOLswx7+88LL7Rfc6FVNd+9NanKmx0AUOwAgGIHABQ7AKDYAaDYAQDFDgC+3OM5O/VpKsiTSAppmhyusbrGkXraun0dthggUlW3ftyi00DfvJ9dUhWRWzt1EdFyStaWSGkBps8lpcq8vfVY3nhbzFOKvWWYnrP9J7fQ5w8Nk8YeiGf+lfIjffDdtd7m+TBNxc6+Giklj/0GX9XPzibP2HheyeXWbmM/fnHde2DTN9sXprqrW3y+vAy4i6hL7FN4e+JC8GYHgI+xAECxAwCKHQB8lj/fcqBe/gF5Mg2IC7+xDoA3OwCg2AHgY+wHfGjd+fm05Xdaf7ptff7TMlloaSLn7twN8ns72fVcXjhHM3vXvMDtDg/hylf3s8vjcsktNCYfP+Th4s0OAB9jAYBiBwAUOwCg2AEAxQ4AKHYAcNDjOTvXNslqWaImYqFu5vhQqr/aNSSb6i99vS13M9l1SV6tR5xsPPV8ejYuGVYgrrfDRoOzpSvgs7+bW0pM3VPZkifV1eHv7dW8/eahnxgqnMfWNGc4vZ9s22P5Vnw0flHY86F+drzZAQDFDgAodgBAsQNAsQMAih0AUOwA4Atc3s9uEmXKiZu7uZv988Y+Omco/ew+wanzxsoz88a+8mQnadP39rN75VNPPzsAoNgBwHd9jD3zxVjrq3/4nRzn97MA8GYHABQ7ABQ7AKDYAcDX+cMQYI+eETtpa7uzV2lpn9rbpanVGJurJH/4AdBbaEWnIp4TfDqcbNvuTVfPKPdua+oJ6vp4ntHPzn/yzup2TUTEU2i6WPtL5hPRfgQmIj70ZDTtS1xekfyzcFP1fpGhL2FeaDrcOZP5f3feTrzZAeBjLABQ7ACAYgcAFDsAoNgBAMUOAA76d3N2qqWJgLu3QJG7a0j0HN5yy0xth62WfrBMPfquDmCTBBPOudNm88aaWZxl+HA/u7zN0tFvXHj3B/2aC62qZTLm0LaPNzsAoNgBAMUOACh2AECxA0CxAwCKHQB8scdzdurTVJAnkRTSNDlcY3WNI/X0XROAxthRSQmVTmb5rFMfhN4GLI1b+K/ab0vdtv9esTqetd2Y3moqKYla60EWxrk2LHvJCEyvSFnjhL080rjNYlu5tgHVVMf5p84bawdum7/i0/lb3bXe5vkwTXs/tWdONs4bm1Jy8T6atZ+d1tvNtc8mlTyZpHLHubpqHgpdG0m1cJ2832YiJv+JV9rH80out7buS5Keqe6q71cleRlwr49a7ycorprKINY44c7biTc7AHyMBQCKHQBQ7ACAYgcAFDsAoNgBwEEf2s+uzaq5Z82Ysmlpqft5MXHRaaBvqZ/dK+JGPeQltaHdBdt/aM1f1tJucb5RM5N/tXOfh9lyT9+ye2+M6I9NE3zkOjJvLABQ7ABQ7ACAYgcAFDsAoNgBAMUOAK71/yTnlqgqMMf/AAAAAElFTkSuQmCC'

bt_i_decodad=base64.b64decode(bt_i)
abort_decode=base64.b64decode(abort_i)
bg_decodad=base64.b64decode(bg_i)

root.minsize(width=410,height=390)
root.maxsize(width=410,height=390)
root.title("SHUT DOWN AND RESTART MANAGER")
root.iconbitmap("icon.ico")
file=PhotoImage(data=bg_decodad)
bt_image=PhotoImage(data=bt_i)
bt_image=bt_image.subsample(2,2)
abort_image=PhotoImage(data=abort_decode)

label=Label(root,image=file).pack()

hours_i=StringVar()
min_i=StringVar()
sec_i=StringVar()

hours_o1=StringVar()
hours_o2=StringVar()
min_o1=StringVar()
min_o2=StringVar()
sec_o1=StringVar()
sec_o2=StringVar()

hours_o1.set("0")
hours_o2.set("0")
min_o1.set("0")
min_o2.set("0")
sec_o1.set("0")
sec_o2.set("0")

frame1=Frame(root,border=2,bg="#00b8e6",width=330,highlightbackground="red",highlightthickness=4,height=40).place(x=39,y=10)
frame1=Frame(root).place(x=1,y=50)

lbl1=Label(frame1,text="SHUT DOWN AND RESTART MANAGER",fg="black",bg="#00b8e6",font=("Blanka",13)).place(x=49,y=17)

hours_combo=ttk.Combobox(root,width=7,textvariable=hours_i,font="9",)
hours_combo["values"] =("HOURS","00","01","02","03","04","05","06","07","08","09","10","11","12")
hours_combo["state"]="readonly"
hours_combo.current(0)
hours_combo.place(x=34,y=70)

min_combo=ttk.Combobox(root,width=8,textvariable=min_i,font="9")
min_combo["values"] =("MINUTES","00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")  
min_combo["state"]="readonly"
min_combo.current(0)
min_combo.place(x=150,y=70)

sec_combo=ttk.Combobox(root,width=9,textvariable=sec_i,font="9")
sec_combo["values"] =("SECONDS","00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")  
sec_combo["state"]="readonly"
sec_combo.current(0)
sec_combo.place(x=270,y=70)

radio_i=IntVar()

radio_b=Radiobutton(root,text="SHUTDOWN",value=0,variable=radio_i,bg="#00b8e6")
radio_b.place(x=85,y=110)

radio_b=Radiobutton(root,text="RESTART",value=1,variable=radio_i,bg="#00b8e6")
radio_b.place(x=225,y=110)

frm=Frame(root,width=40,).pack()

timer=Label(frm,text="TIMES LEFT TO SHUTDOWN / RESTART",font=("Arial",15),fg="red",bg="#00b8e6")
timer.place(y=200,x=15)

ent_h1=Label(frm,textvariable=hours_o1,font=("Arial",25),fg="red",bg="#00b8e6")
ent_h1.place(y=230,x=80)
ent_h2=Label(frm,textvariable=hours_o2,font=("Arial",25),fg="red",bg="#00b8e6")
ent_h2.place(y=230,x=110)
ent_h3=Label(frm,text=":",font=("Arial",25),fg="red",bg="#00b8e6")
ent_h3.place(y=230,x=140)
ent_m1=Label(frm,textvariable=min_o1,font=("Arial",25),fg="red",bg="#00b8e6")
ent_m1.place(y=230,x=170)
ent_m2=Label(frm,textvariable=min_o2,font=("Arial",25),fg="red",bg="#00b8e6")
ent_m2.place(y=230,x=200)
ent_m3=Label(frm,text=":",font=("Arial",25),fg="red",bg="#00b8e6")
ent_m3.place(y=230,x=235)
ent_s1=Label(frm,textvariable=sec_o1,font=("Arial",25),fg="red",bg="#00b8e6")
ent_s1.place(y=230,x=265)
ent_s2=Label(frm,textvariable=sec_o2,font=("Arial",25),fg="red",bg="#00b8e6")
ent_s2.place(y=230,x=295)

abort=Label(frm,text="IF YOU WANT TO ABORT SHUTDOWN / RESTART PRESS ABORT",font=("Arial",10),bg="#00b8e6",fg="black")
abort.place(x=1,y=270)

lbl2=Label(frm,text="Desinged by Boranno Golder",fg="white",bg="#00b8e6",font=("Arial",15))
lbl2.place(x=70,y=360)  
     
abort_out=0    
def abort():
    os.system("shutdown /a")
    root.destroy()

def countdown():
    try:
        user_input=int(hours_i.get())*3600+int(min_i.get())*60+int(sec_i.get())
    except:
        messagebox.showwarning("Warning","invlaid option")

    def shutdown():
        os.system(f"shutdown /s /f /t {user_input} ")

    def restart():
        os.system(f"shutdown /r /f /t {user_input}")

    if radio_i.get() == 0:
        shutdown()
    elif radio_i.get() ==1:
        restart()

    while user_input  >-1:
        hours=user_input//3600

        ext_sec=user_input-3600*hours

        min=ext_sec//60

        sec=ext_sec%60

        def n1(a):
            d=a//10
            return d
    
        def n2(a):
            d=a%10
            return d

        hours_o1.set(n1(hours))
        hours_o2.set(n2(hours))

        min_o1.set(n1(min))
        min_o2.set(n2(min))

        sec_o1.set(n1(sec))
        sec_o2.set(n2(sec))

        root.update()
        time.sleep(1)
        user_input-=1

btn_start=Button(root,width=50,text="Enter",height=45,image=bt_image,bg="#00b8e6",command=countdown)
btn_start.place(x=170,y=140)

btn_abort=Button(width=50,height=45,image=abort_image,bg="#00b8e6",command=abort,)
btn_abort.place(x=170,y=300)

root.mainloop()