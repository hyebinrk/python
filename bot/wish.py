import random
async def send_riku(update, context):
    photo_url = ["https://i.pinimg.com/736x/a1/44/7a/a1447a6f5430fb7fe63f0fe3ee6cb2fd.jpg",
                 "https://i.pinimg.com/736x/5e/f1/b4/5ef1b4db337794a1c0c6a9f68aad3f6f.jpg",
                 "https://i.pinimg.com/736x/19/63/48/196348487f2228a7cc3e08706a031b6a.jpg",
                "https://i.pinimg.com/736x/f3/00/43/f300430b2b8699fd38508916d1ee102c.jpg",
                "https://i.pinimg.com/736x/52/66/de/5266de227332eb4c2f488b7a65768417.jpg",
                "https://i.pinimg.com/736x/dc/5a/e7/dc5ae76d8c9d8539ae8e167158621095.jpg",
                "https://i.pinimg.com/736x/05/88/fc/0588fc199b218c992550bdc81ab412b5.jpg",
                "https://i.pinimg.com/736x/4c/b7/36/4cb736f30b4228e50f884b9c5b7d1fd9.jpg",
                "https://i.pinimg.com/736x/fb/f6/f2/fbf6f281e8cde5c328334144eb61c281.jpg",
                "https://i.pinimg.com/736x/0f/ed/ef/0fedefbdc3a50653f572c039aea72550.jpg",
                "https://i.pinimg.com/736x/fd/37/27/fd37270768c915f1d0929277189635af.jpg",
                "https://i.pinimg.com/736x/c7/27/2c/c7272cf59ea42f9a5631045bbda90f24.jpg",
                "https://i.pinimg.com/736x/52/09/8d/52098d659d9f18ae0265593a5967c535.jpg",
                "https://i.pinimg.com/736x/22/bb/64/22bb6493a4abc87196bd664b59be057f.jpg",
                "https://i.pinimg.com/736x/3a/7d/26/3a7d26ede7d25d52f00ff9c878523a9a.jpg",
                "https://i.pinimg.com/736x/e1/e1/75/e1e175d6d2ff4336b7f67268c244789f.jpg",
                "https://i.pinimg.com/736x/35/43/25/35432544992e6c004455b10228779bee.jpg",
                "https://i.pinimg.com/736x/2c/73/f2/2c73f2d136a84973c432f8be0dc4c360.jpg",
                "https://i.pinimg.com/736x/d8/ee/1f/d8ee1ff2b48a94774fc735fb4f840d61.jpg",
                "https://i.pinimg.com/736x/3b/db/59/3bdb59b81f8f66b48e0df477183c6b16.jpg",
                "https://i.pinimg.com/736x/b9/d3/03/b9d303571a39d91a20c61d439dc59e13.jpg",
                "https://i.pinimg.com/736x/34/ad/26/34ad2601dad49240280f995099b346e9.jpg",
                "https://i.pinimg.com/736x/d0/ee/c2/d0eec276f4c8469fa88792123bef2443.jpg",
                "https://i.pinimg.com/736x/01/b7/de/01b7de6d9787d09380a181706ed3f788.jpg",
                "https://i.pinimg.com/736x/5b/49/f2/5b49f2b28ecc15c662aef2b038ba2a4e.jpg",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfNTUg/MDAxNzQyNzc1MjA5ODc3.t0kTXHqw4Gg2SWVktH_TZEg3LV8ayBhf7dwPvCSE_24g.f1hLG2zqees5DI7J_fRVd5Sf02e_Wqo_KdtS2whqpoEg.JPEG/weverse_20250323221155_2765809173.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfOTgg/MDAxNzQyNzc1MjA5NTUz.UQ0nATpDdXa1BN8tXPQpx1OmdCezUx2kcyDD8071Z6Ig.rHAhplf-iDwnf0jkP1ohgptiVW4kd2TM2A7JTS9r16gg.JPEG/IMG_5272.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMjk2/MDAxNzQyNzc1MjI0MzE4.1X88pkyTdiHE--dk1N1h2i0uUtFC8lAsUmj-qHbpmq4g.jH0vQ9DGJ_llZPFwFYF0rW0uP_rysyp3d9WyRDgRPaIg.JPEG/IMG_5271.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMTU2/MDAxNzQyNzc1MjA5ODAw.pT7JY1HVBdThkQgcdFp6qnaaRiagF5dvvJacPyUIM4Qg.irZfj1wEGw0Wvd2NHCTHtYJe8CkyMjEFsS7we461i84g.JPEG/IMG_5269.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMjgy/MDAxNzQyNzc1MjA5MzMz.zaEK12qV8rCLU5Aekbs3DraYzJCTB7dX7sRzljIFQicg.C7n9a1EHiC7BvHtSnqJoQAn2Ysovy8bO0qAn5W_lP-Ag.JPEG/IMG_5268.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMjgy/MDAxNzQyNzc1MjA5ODE2.dvA6VHgzk17GeZexbLMM-VFAw9KFayIMqvfRuul14UMg.nfxS4ycVnX3N2dlrGZODmJ4JkmhCB4n3Vw3UbVCGZPwg.JPEG/IMG_5267.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMjEw/MDAxNzQyNzc1MjEzMDE1.2gHQNmscWs3IEERFs5eTnmkgh2rTgX88rQw_rClQDPkg.GIIrL8kFya-SHm59bqklNKBjEoRqyAwJXdqaxDsr9e0g.JPEG/IMG_5263.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMTEy/MDAxNzQyNzc1MjEyOTAx.R-LwySsLXQw_i28mMNERn1J-sr3rywF8wOnqz6-PIpMg.CZHqo4BoIC0C6donMsG7iTNLjAP__vaOXVxJSmmpgOog.JPEG/IMG_5262.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfNDIg/MDAxNzQyNzc1MjEzMTIw.glXDmgUZ5zDILAiIIb4bQsvf9dJz_9V1AhKa1fOpsEUg.NwBbGzWGrvX81nddCty-fdtUvfxc7t8PAAHDADucNrkg.JPEG/IMG_5260.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfNzcg/MDAxNzQyNzc1MjE2NDEz.pZrH8IG6CoUMCgT_CB9GFqivkz3kbtPc0Ha18kTPm7Ag.w2Ix_Z-99WJjsaKzgFuxtdZcuGeOhb1SA6EuYDlglEIg.JPEG/IMG_5252.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfNzEg/MDAxNzQyNzc1MjE5MzU4.FtnckoOW9d5He66GLtUcC7Teh3qeT18ldB37hvs3vDQg.1YNlUdNDq-woHFqRI4HQL3Dk7iZzZGcL6VBu_Dzj6lQg.JPEG/IMG_5251.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfODYg/MDAxNzQyNzc1MjE2NDE1.Gdh3meVkElM5AnPfyKEH1ZXIzcbWhsnDBuoMVfaWI30g.zjo6EZeW2xNvuKR3XPDKpUh1a5cj20dsYVvTyzrMp5Yg.JPEG/IMG_5250.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfNzIg/MDAxNzQyNzc1MjE2NTI0.vmQUEeVUVVbJaSj_DKjmR2JLdzByX0g_FHhpvKgpFrQg.vK0OG2SAey9MVBVDBBUOsLZHqhbFnOP28o0TdL3a94Mg.JPEG/IMG_5244.JPG?type=w966"]
    select_photo = random.choice(photo_url)
    await update.message.reply_photo(photo=select_photo,caption="리쿠 사진이 도착했습니다‼️📩")

async def send_sion(update, context):
    photo_url = ["https://i.pinimg.com/736x/0c/0c/78/0c0c787ce6b32cd842d36413c06a17ad.jpg",
                 "https://i.pinimg.com/736x/33/11/18/331118b87b3ec4c08fa69e75996d93a9.jpg",
                 "https://i.pinimg.com/736x/03/9e/30/039e3035406cd5046bc99765fce1d210.jpg",
                 "https://i.pinimg.com/736x/22/e0/e4/22e0e41fb1f7c0c4866af995f9041a74.jpg",
                 "https://i.pinimg.com/736x/52/1b/70/521b708fa1e0654317b83c79b62577f2.jpg",
                 "https://i.pinimg.com/736x/d2/d6/b5/d2d6b5340ebaf70345bde86d0d2c3d59.jpg",
                 "https://i.pinimg.com/736x/48/5a/10/485a10b239bee998d7e7f81634f6063c.jpg",
                 "https://i.pinimg.com/736x/f2/31/9a/f2319a23c666c505bed7cb75a58393bc.jpg",
                 "https://i.pinimg.com/736x/1e/dd/96/1edd9653beb1422b184c22a9c1c17698.jpg",
                 "https://i.pinimg.com/736x/f0/49/76/f04976752a226e0e86dada18a2d24227.jpg",
                 "https://i.pinimg.com/736x/e5/49/dc/e549dcd1e986ca7afe6c000afb8903e5.jpg",
                 "https://i.pinimg.com/736x/2b/a4/5e/2ba45e1c7e1db51073e73220f0299df3.jpg",
                 "https://i.pinimg.com/736x/8c/19/e7/8c19e708bdded4933ee843f0c2f043dd.jpg",
                 "https://i.pinimg.com/736x/75/45/1c/75451cffca69fd32cbb85cfc407e9fca.jpg",
                 "https://i.pinimg.com/736x/40/37/87/40378727958262ed29958120155d5251.jpg",
                "https://i.pinimg.com/736x/52/56/04/525604ba06d30961bf8da4fc36a03786.jpg",
                "https://i.pinimg.com/736x/af/6e/51/af6e5161451355ad782e966c3f7f0d2c.jpg",
                "https://i.pinimg.com/736x/1d/32/8f/1d328f33aa804873af3ef08f464f7813.jpg",
                "https://i.pinimg.com/736x/a0/20/a2/a020a2db880c6cbad833ed7fccbcdf84.jpg",
                "https://i.pinimg.com/736x/cc/e3/c1/cce3c1499fcb650f0c44f4f995322ddb.jpg",
                "https://i.pinimg.com/736x/c2/df/6c/c2df6cb1e402ea66ad0472c2a3718019.jpg",
                "https://i.pinimg.com/736x/52/56/04/525604ba06d30961bf8da4fc36a03786.jpg",
                "https://i.pinimg.com/736x/63/1f/38/631f3818595ed98ca8e06bcfea8071e8.jpg",
                "https://i.pinimg.com/736x/24/94/4b/24944b9d8e3c76bdf160013fbc223363.jpg",
                "https://i.pinimg.com/736x/80/a0/30/80a030e00765562d0552dcf7ea0d0c34.jpg",
                "https://i.pinimg.com/736x/f4/83/80/f48380ff179e0d426eac03259ae43cad.jpg",
                "https://i.pinimg.com/736x/47/04/8c/47048ce73ca0b4431e09fea26b41b426.jpg",
                "https://i.pinimg.com/736x/e4/64/8e/e4648eb27a25dc09820f611029d6890e.jpg",
                "https://i.pinimg.com/736x/b8/d5/82/b8d582802c13da3d3c19ad5142a466f8.jpg",
                "https://i.pinimg.com/736x/05/f1/54/05f1542ae50bfe47dcd7648bfdfe7cb0.jpg",
                "https://i.pinimg.com/736x/40/3e/b8/403eb8b35ab1660dbac44161947f70ee.jpg",
                "https://i.pinimg.com/736x/fb/c6/e5/fbc6e5d1c9775af8ec8cb9cd612ee5b7.jpg",
                "https://i.pinimg.com/736x/11/df/ec/11dfecefacf4ec29f65b37eaa1a1084c.jpg",
                "https://i.pinimg.com/736x/a2/1d/79/a21d7969df07d2b2b28eb721c57c6ce2.jpg",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMTE2/MDAxNzQyMDM4NTQ0MTAz.dqidcZOALrXHwHholCX34NWOQUHutxTSC6rtQeC2biog.4aoL-ol-NGi2rOu-KWoLTxnUayUz-fwcfjN0Px7Qrskg.JPEG/photo_2025-03-15_20-29-40.jpg?type=w966",         "https://postfiles.pstatic.net/MjAyNTAzMTVfMjMw/MDAxNzQyMDM4NTQ0MDg5.V5JQrpYMd_TayyWlWe_D5PKsSHZEl4SeYgUB09nUEdQg.wzmDjfCk4elpmVo4E8cDkKivwkHKH_tkVUmRQkcamQEg.JPEG/photo_2025-03-15_20-30-50.jpg?type=w966",         "https://postfiles.pstatic.net/MjAyNTAzMTVfNCAg/MDAxNzQyMDM4NTQ0NDg2.i33OFL0VBwj78e7Ixec72GIbq6VNuBbJcAJE6wTfZawg.uf0dyBRxTTyouConsTsdAq_sH_2i--GDeRZBJcMA3V0g.JPEG/photo_2025-03-15_20-30-56.jpg?type=w966",         "https://postfiles.pstatic.net/MjAyNTAzMTVfMjg3/MDAxNzQyMDM4NTQ0NDgz.GaDF4DyGLSi3z7WfN6BNRLPXoq5MXEtZJOUU8zT69bog.xD71I_43ju7R8BLcMdjFFdDeNsh4_irRUvcDfL0Bz2Yg.JPEG/photo_2025-03-15_20-30-59.jpg?type=w966",         "https://postfiles.pstatic.net/MjAyNTAzMTVfMjE0/MDAxNzQyMDM4NTQ0NTg5.22Nwss9wFRi3YdsgSorYm9Ri9LRDyYcRdcWn6APrzZAg.OkWSMKam923u_2lgXaJ8KHPvNB6Z6Ym1nAcwZs75XAMg.JPEG/photo_2025-03-15_20-31-01.jpg?type=w966",         "https://postfiles.pstatic.net/MjAyNTAzMTVfNTEg/MDAxNzQyMDM4NTQ0NTkz.VRALakXhjpyt7SdxAvPgN0DUScsS9gzQ_piimV0QfF0g.cQiQCbK_AHdMvQ_ZqDHN_8314PUtoWD5B2bLycUQmKMg.JPEG/photo_2025-03-15_20-31-04.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfNzQg/MDAxNzQyMDM4NTQ0NjA1.Mga075pxSbB7ErrdwoyTCKbPt30HT5t-H0MNvk2qSD8g.hP_QPc2YhGy29WahCWKyPVSv9ybQuYK542-bUllPldwg.JPEG/photo_2025-03-15_20-31-07.jpg?type=w966",         "https://postfiles.pstatic.net/MjAyNTAzMTVfMTgy/MDAxNzQyMDM4NTQ0NjA0.5xza8C85XxlAzA98IC0WBCtWuJPUsHzr3PnVglZKn88g.zpFQ4M5N88mutcdIcG5cx3TkeERAh0MQczBjAOSjwc8g.JPEG/photo_2025-03-15_20-31-13.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfNzQg/MDAxNzQyMDM4NTQ0OTg5.hLaRrFSox8gN60DCb4Bwe0lFwrEL9ID43d1b7QvkGl0g.ZpfsuoZ9GtchivpsFsbU1CSKq_n8yWfJSBVxFjkQP6gg.JPEG/photo_2025-03-15_20-31-16.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMTIg/MDAxNzQyMDM4NTQ0OTg3.x2L2hGBQknIthavENhESl1eWsFBxcHF3d24a1hfGjm0g.tQ6PjfBDuw8CE14ofvhWDmi2sQMpvmYdPUY4Pz_Ihfgg.JPEG/photo_2025-03-15_20-31-18.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMTE5/MDAxNzQyMDM4NTQ1MDQz.63ljyQUbu9IIc2mcqLyo4W4B7leWn0rEDBxFiFwC_jEg._CetgkgynqDRkH5FK3cLaIaK3ejhq9zOzOMvokYtut8g.JPEG/photo_2025-03-15_20-31-21.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMTM2/MDAxNzQyMDM4NTQ1MDg5.DuDp905xRSobxUYZQZCsAh9Ol85RMRc9UFS6egpQ7YIg.8OJvcQDJ5eAAv6BTxD46b-o6m4_YZkxUgX6M1MT5xKAg.JPEG/photo_2025-03-15_20-31-24.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMTc4/MDAxNzQyMDM4NTQ1MTA1.08_5qgYZUfJvU2RapOANQzlDIGCiAwZEJ98ZeBJ1_Hcg.sjF0f9xcKEUft1ylSVkDj3GQiEJFgN2rQtliEMW7du0g.JPEG/photo_2025-03-15_20-31-26.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMTc4/MDAxNzQyMDM4NTQ1MTA1.08_5qgYZUfJvU2RapOANQzlDIGCiAwZEJ98ZeBJ1_Hcg.sjF0f9xcKEUft1ylSVkDj3GQiEJFgN2rQtliEMW7du0g.JPEG/photo_2025-03-15_20-31-26.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMzQg/MDAxNzQyMDM4NTQ1MTA0.Dn-tftoHDWRRkRTVBqOWgbS8eBSkvI3tVXXgQOGYxV8g.htVf2zcYb9EgpkJCgMYRvKCExNaLhEKLuMYyBse_W7sg.JPEG/photo_2025-03-15_20-31-28.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMTY3/MDAxNzQyMDM4NTQ1Mzgy.1bd0KP1q-amToLyMfirqKhWHqt6fnKKpB4HjAAZF_C0g.ie5oH7CYSbAQU02TIftuSTfKe4SRZmYg0bH3LJCm4_wg.JPEG/photo_2025-03-15_20-31-33.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMTA0/MDAxNzQyMDM4NTQ1NDY2.uySgPo-LD114LRNs8tSanxKPzRyARV-QnG8LJn5KuTog.z71T5UCcWliMs-6wSIgck5iSkDceRPE5neCPTVLqCdkg.JPEG/photo_2025-03-15_20-31-36.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMTE3/MDAxNzQyMDM4NTQ1NTY5.cJnsNP-BDmhhduL4yILhlC6RlDPUQFQqHA3JO3eBEzYg.pqDz4RHDYHgOF6HsSYiX0haiks1QzF--sg4reTd-u6cg.JPEG/photo_2025-03-15_20-31-38.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMjQ5/MDAxNzQyMDM4NTQ1NTY4.IIOFZuOddzWj-9tcELwkF-cc0pjELTi8flpJ2k-L8L8g.va1U5NEIqBT2FQPBAZG0_GvgLL3uYuBRYH3euyUfj3Ig.JPEG/photo_2025-03-15_20-31-41.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfNzgg/MDAxNzQyMDM4NTQ1NjAx.0H_mdTuZREtTAvuaZ-Ggt6DiA8EalN-ixSDpjX9mOeEg.sr-jiJlxKW8SzYz0sLYc_li-0QGH8hfWTbTLMcoGFmMg.JPEG/photo_2025-03-15_20-31-44.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfNDEg/MDAxNzQyMDM4NTQzOTYz.zqGn8UOSG1YJx0IlBIHy_dkNaqykicLsiFzATE3DDhMg.zYwzzeOBJL30XtfWVfFNyaSP5m1YB-2rOKuGH4OYvQYg.JPEG/photo_2025-03-15_20-31-46.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMjk5/MDAxNzQyMDM4NTQzOTA2.qXlXc0_-QzPQ4fGdKku9izdxLENxAxD4AgCtUHvXzjcg.o4kAf0JY4TGIwzQr5bbf36oCJ8lb1mkgkvA8t7oZlWYg.JPEG/photo_2025-03-15_20-31-49.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfMyAg/MDAxNzQyMDM4NTQzOTgw.iu8x3tv7HfJP4hxb314Ys__FjLNOVw-4KoMHt0RYgvAg.wM43mbsuIxYlU7CMHSQGFrOgI6KNLOSUtvkkmkcGx_kg.JPEG/photo_2025-03-15_20-31-51.jpg?type=w966",
"https://postfiles.pstatic.net/MjAyNTAzMTVfNTYg/MDAxNzQyMDM4NTQ0MDYx.d6w3tAeZXOK2Bk4b5lmrttjc13frqm5JRWc47UWi6usg.d1X6byevhR2oX70Q5SfGazTVCvkN5EiYJARBTIGaV2Mg.JPEG/photo_2025-03-15_20-31-53.jpg?type=w966",
                "https://i.pinimg.com/736x/85/a1/7f/85a17f20b7d35ed914d863fc05f878f7.jpg",
                "https://i.pinimg.com/736x/55/2a/6e/552a6e7dc0280ca08acada51ac7139bb.jpg",
"https://postfiles.pstatic.net/MjAyNTAzMTZfMTIg/MDAxNzQyMDk4NTY5ODQ0.JhU91PlOmumvCBxVEmwBYGnXxuijZwdA_rY2jli8CLIg.trFLCdveKtHp1m1wPNKfJt9BjKUEIxkk1Ooi5BcUDk8g.JPEG/photo_2025-03-16_13-15-06.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMTU0/MDAxNzQyODAwNjkwMzc1.8T2NZ7QuKLhWgHQORouO6OT51f2U-kZ-RVtujACHJrgg.E2UAROlBNrQU-PfuQe_RM3mxNi74aDbCPku54SVNkuMg.PNG/image.png?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMTQ0/MDAxNzQyODAwNjkzNTkw.anjOf5xDVG-NT7c58yZ8jNoJ3S59irfHeKh_2YK5lF4g.e3a80y_BACnZf5360Y6TPpZ2Yscru8qbuz92sZyQsDcg.PNG/image.png?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfODEg/MDAxNzQzNDY2Mjc3MTQy.fssmrqsvyrMVABmXcsJoAFG7Fn9IF81FF3W2u2AWfNUg.YqSr3-YWXqZU9yYrEJrD7KbJyKyoGamyIocc_W0cx8Yg.JPEG/photo_2025-04-01_09-10-45.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfMjM4/MDAxNzQzNDY2Mjc3MTQy.20RTI9O3i-4VkPMemO0lu4E5nlBHZgVDBneq4WRMV2Yg.PMqbrjhPG44eTsw8ft4hl_LkdcHb5vXNofG5ihFIBfsg.JPEG/photo_2025-04-01_09-10-43.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfOTQg/MDAxNzQzNDY2Mjc3MTU1.NP3s-DqGYFO2vkd8WF6IX3VXaYko3GmlOCFU7ATzJ54g.GCWY_2MCC2jKV4hcDuJfcnv-cq_As_1KAVA2ve_eXZsg.JPEG/photo_2025-04-01_09-10-42.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfMTY5/MDAxNzQzNDY2Mjc3MTQ1.GSK_wkR8B9pBjdC8e9hiYBM-sB7cApk0tbzAwkCb7K0g.5--QeG29WmArBMaapO6P6RdViY2G2G18ksUMDY63lXsg.JPEG/photo_2025-04-01_09-10-39.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfMjAw/MDAxNzQzNDY2Mjc3Mjg5.eg9bOm5-3GRQoIkyeLUbeDbfKOkal47znwtTg0seYTEg.Az2sP_Bt03JADTNDEWa_-tkyCAnJ3aoMx0OauuHpfDUg.JPEG/photo_2025-04-01_09-10-37.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfMjUw/MDAxNzQzNDY2Mjc3MzU4.-2bUR-CObcMZogkK65V5e-k8ialgihyvhS6jRW70olYg.vFlzLGEx5WjF_G0AuIFhErr_JctUtCCCvQrjOivwR_8g.JPEG/photo_2025-04-01_09-10-35.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfMTk4/MDAxNzQzNDY2Mjc3NTM1.P9ukntE6y2KjIzlS6HDMnk03ZCXjBzo2zyRxqjQWnQ4g.JvP30BNsY7KEjEC4o2yLIn0IE4b_Iu1_rmmkOeCibhUg.JPEG/photo_2025-04-01_09-10-34.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfNDMg/MDAxNzQzNDY2Mjc3NTY1._OnUJWWO20WqSaVb9rQdTfREWl7PTbnmX-wmzHOddwIg.qZcikmoiSyYY_IteYHXq7Lhj_ES1ONLO89qUwqb7lmog.JPEG/photo_2025-04-01_09-10-32.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfMjE3/MDAxNzQzNDY2Mjc3NTk0.EjZ9FhDq9IeFmrmiURzjLkEH4kImJPXXU-2A-fGKKn8g.Yv4KXGiejdRvEH94Pt4aUVKwZ0fssod9Kmp3SNVdStog.JPEG/photo_2025-04-01_09-10-31.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfMTQ4/MDAxNzQzNDY2Mjc3NjI0.jStIPhtlm5gNNG90metWeAN2d6Sg4RLZ20oKLouMFHQg.hq03a2JhYgpU_YA-QDmdi3-DUvsOn3zo_YvRj1QNaSIg.JPEG/photo_2025-04-01_09-10-29.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfMTA2/MDAxNzQzNDY2Mjc3NzI4.1qHYv0gRD-LhFhUFh4drcgG5D5WJDDWPHEA-tWrIJaYg.-vPlHpsJm-tOMUqamgfSj4HSLuDFb8YeDpuP-K3GJ7Ag.JPEG/photo_2025-04-01_09-10-27.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfMTY5/MDAxNzQzNDY2Mjc3ODU3.OmwcxIJDMNd0UA8FWIpDrM4bJS5HaxjefXCywp_FIZcg.dQBHJnZLtyL270l2o5P6oVebapTwbXizHBPFXNq2BHMg.JPEG/photo_2025-04-01_09-10-25.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfMTI0/MDAxNzQzNDY2Mjc3OTU3.CYOg0VlCy1eGnnNnzpw9YSMDWFbOu9DAwRcovhd1XRQg._YLkN0DnBXbSHJ9iNQSEKCXbsuQlsRgh-rp7n3vrgx0g.JPEG/photo_2025-04-01_09-10-23.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfMjYy/MDAxNzQzNDY2Mjc3OTc2.HSvgZoZvD77fNZwGQIOn7lVklbBDB49GX2wC19pVhkwg.QlrhkNfgt0afSXhBb7m1HSZ4UPrS7sDmYDKjro_fseEg.JPEG/photo_2025-04-01_09-10-03.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTA0MDFfMjkw/MDAxNzQzNDY2Mjc3OTg2.k3lHvmia4zPmJvqviEMWoTkKspnlt5aE3uZdxcxVP_Eg.YXTr2Zt86LIrRfQVCT3dFBOqJMzaKY1wrfMynHEJM2Ig.JPEG/photo_2025-04-01_09-09-59.jpg?type=w966"]                 
    select_photo = random.choice(photo_url)             
    await update.message.reply_photo(photo=select_photo,caption="시온 사진이 도착했습니다‼️📩")

async def send_yushi(update, context):
    photo_url = ["https://i.pinimg.com/736x/63/1e/87/631e8785717d2071a9141d61ab0d991c.jpg",
                 "https://i.pinimg.com/736x/ae/d4/af/aed4af1ca7ec9322a6e43e682ab47e4c.jpg",
                "https://i.pinimg.com/736x/c8/21/f5/c821f5e3fdc9f151029211afbdca8a79.jpg",
                "https://i.pinimg.com/736x/40/fa/b7/40fab78012bd70e1dff449598da826a3.jpg",
                "https://i.pinimg.com/736x/6f/51/45/6f5145a1be8807129547bdc61fa965cc.jpg",
                "https://i.pinimg.com/736x/8b/7c/33/8b7c330e1b403b7bc5b21b597c1af700.jpg",
                "https://i.pinimg.com/736x/c0/68/5b/c0685bfa6e7c678a946b611086880c0a.jpg",
                "https://i.pinimg.com/736x/4a/a7/03/4aa703dcb49552e07d4a5c820de83340.jpg",
                "https://i.pinimg.com/736x/bb/60/4a/bb604ab9957efda324a7ee8f5b44e576.jpg",
                "https://i.pinimg.com/736x/ae/d4/31/aed431305c3b8d4030068360f6a871b4.jpg",
                "https://i.pinimg.com/736x/85/8d/06/858d06cec30e77a0b747eee9b09faba9.jpg",
                "https://i.pinimg.com/736x/93/b8/3b/93b83b9449dfe0cf7d4f7024e02d07e3.jpg",
                "https://i.pinimg.com/736x/39/f0/fa/39f0fa3d41f4e3c424d39c7e124a7902.jpg",
                "https://i.pinimg.com/736x/29/87/28/2987283ad0e482509a84650ef55518e5.jpg",
                "https://i.pinimg.com/736x/10/42/58/104258d93e5104f21add7475339bf430.jpg",
                "https://i.pinimg.com/736x/ba/ee/e2/baeee233d1ebf254b5321fabb33986da.jpg",
                "https://i.pinimg.com/736x/7f/0f/b7/7f0fb762d2ae8be333f41ac7df20ac6d.jpg",
                "https://i.pinimg.com/736x/35/0c/d6/350cd6fb7b748b95fa1e93a40e28fccc.jpg",
                "https://i.pinimg.com/736x/75/ff/5a/75ff5a708dad0bac6c63e7ee7548c7e0.jpg",
                "https://i.pinimg.com/736x/df/5d/70/df5d70378f20f22eb3b69140982ff855.jpg",
                "https://i.pinimg.com/736x/1b/32/bb/1b32bb9f03ef1a930dc62b04f69d2ad5.jpg",
                "https://i.pinimg.com/736x/c6/11/d1/c611d1882cea72137c149828a1985391.jpg",
                "https://i.pinimg.com/736x/0d/2f/63/0d2f6333b88f64efce28696e2f15b0ab.jpg",
                "https://i.pinimg.com/736x/3d/be/19/3dbe19dccb9840bd0a525fe10efa503b.jpg",
                "https://i.pinimg.com/736x/04/19/bb/0419bbff051f005fe1e2fb239a93b170.jpg",
                "https://i.pinimg.com/736x/4f/8f/d8/4f8fd8c352ec6087671a44d48ed7f35f.jpg",
                "https://i.pinimg.com/736x/8e/d1/bf/8ed1bf97bc5893924e7cfb4d62066473.jpg",
                "https://i.pinimg.com/736x/ea/1d/32/ea1d3270ca8fa362f7a94e026b72a22f.jpg",
                "https://i.pinimg.com/736x/9f/09/2d/9f092d7c5fff8465eb3e9eaf6ced7f29.jpg",
                "https://i.pinimg.com/736x/71/5c/30/715c309833cbcb1ad003513942876059.jpg",
                "https://i.pinimg.com/736x/54/32/fb/5432fb53913c6f4555998bddaa7c2c9d.jpg",
                "https://i.pinimg.com/736x/31/dc/68/31dc6852d887a588d3eb272c44b30165.jpg",
                "https://i.pinimg.com/736x/a6/70/7e/a6707e1c60a870b960d6644c12aec29e.jpg",
                "https://i.pinimg.com/736x/6b/72/04/6b72049e51b4dc0de9d9f80b3efefd26.jpg",
                "https://i.pinimg.com/736x/5a/c0/6f/5ac06f10e2271baec310ea08df672339.jpg",
                "https://i.pinimg.com/736x/c7/f6/47/c7f647000495fd766b7134d15e456b39.jpg",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfNjgg/MDAxNzQyNzc1MjI0NDEw.S1Up0Bepp5vv9DZOutwxi5FPflDqy60-UWmeZxRo9IAg.QrjF7eelPSv-_q6YmM-g2k6TWKDEstT35B7J4djTq5wg.JPEG/weverse_20250323221828_2876673140.jpg?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMyAg/MDAxNzQyNzc1MjEzMDE1.bDKSqTbYqSZGI3pMHcJLSdMZv-sd0eIDRCvcVKbFrdQg.rGjG0c8_PdTiGEGc7qOLLgMJdJJidPoKgpDkfAL3m1Qg.JPEG/IMG_7063.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMjk1/MDAxNzQyNzc1MjEzMzgz.ALqLcJrs4wLBBxRgOjFzwhanWAuv72PTQfAMdeduR7Ig.JUK038ERlLzcW2HMp9VROLswqWhhfNRKoX0f4S32kWEg.JPEG/IMG_5254.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMjE1/MDAxNzQyNzc1MjEyNTUx.ywU_wnQNqOeNXDBnxP04vPOJH29q3pxUaOIzbdptzkMg.22UkEO5016dKf7i_37cpExznYEjL9JG6u0XijTE8bo4g.JPEG/IMG_5249.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMjc1/MDAxNzQyNzc1MjIyMzgz.ztkhm5BQPHcUtSNmlhXz7kteh5eko6JNpiuwBbcIJjog.4UxNeWWjD4NfrumX7vpeMDEIIbLQhp-etog4j6ttDAAg.JPEG/IMG_5248.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMTIg/MDAxNzQyNzc1MjE2NTI0.xDeVU5H9yybn2baudNUl3q8p-uewMIoGm81ZX1qxKMwg.I83baIG6mSsreaLIoIZuY4CN2zyC6p1cZ6NaQG0Nyvwg.JPEG/IMG_5245.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfNDcg/MDAxNzQyNzc1MjMwMDMz.YC3Mrt3HwKwdLvcVikTIWR12ldNmknqmyT9Yt0BNP-Ag.VbVg3OqI_uMiTGF1WTUp-Dytrj1yt-cDMggrY0CNzkIg.JPEG/IMG_5243.JPG?type=w966",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfMjQg/MDAxNzQyNzc1Mjc5NDYy.yjmyr-ED0i3hicdlU15Z3X9OEYXgj5xjWrMX8WikC50g.SUFHQVZ-qxWFr7OYmdCJxKPF_rrIcibcWQ-_w3IVfeIg.JPEG/IMG_5285.JPG?type=w966",
                "https://blog.naver.com/PostList.naver?blogId=gpqls3698&from=postList&categoryNo=28#",
                "https://blog.naver.com/PostList.naver?blogId=gpqls3698&from=postList&categoryNo=28#",
                "https://blog.naver.com/PostList.naver?blogId=gpqls3698&from=postList&categoryNo=28#",
                "https://blog.naver.com/PostList.naver?blogId=gpqls3698&from=postList&categoryNo=28#",
                "https://blog.naver.com/PostList.naver?blogId=gpqls3698&from=postList&categoryNo=28#"]
    select_photo = random.choice(photo_url)
    await update.message.reply_photo(photo=select_photo, caption ="유우시 사진이 도착했습니다‼️📩")

async def send_sakuya(update, context):
    photo_url = ["https://i.pinimg.com/736x/4a/03/a3/4a03a33079d0f55cb4c874816cb283db.jpg",
                "https://i.pinimg.com/736x/db/ca/d7/dbcad765e9f23e49837ee22ea97dbf67.jpg",
                "https://i.pinimg.com/736x/bc/b3/ba/bcb3ba1dfb5f9028e4a1d3e310c2ac63.jpg",
                "https://i.pinimg.com/736x/17/0c/21/170c21c4c7b4b782afc9a3e1b4e38078.jpg",
                "https://i.pinimg.com/736x/03/40/a1/0340a187745af2456ac372bff62e84e5.jpg",
                "https://i.pinimg.com/736x/68/12/66/681266d6b51dc021da78d24e458ba95a.jpg",
                "https://i.pinimg.com/736x/cd/05/ae/cd05aeed6473049ea7d8e1a0ea37fc3c.jpg",
                "https://i.pinimg.com/736x/09/5f/5a/095f5a26c3fb930cad067cad566c27fc.jpg",
                "https://i.pinimg.com/736x/72/6f/ce/726fcedfc76474d0127ac13bc3fe8404.jpg",
                "https://i.pinimg.com/736x/6c/3a/c2/6c3ac269b5ebf867c316994d133f1672.jpg",
                "https://i.pinimg.com/736x/2e/4b/2d/2e4b2ddb9ade23f46932908866b720e9.jpg",
                "https://i.pinimg.com/736x/fc/bb/1f/fcbb1fdf586717b0fd50fcf73629739e.jpg",
                "https://i.pinimg.com/736x/e8/e8/53/e8e8539c63e4c1750ac1b9dc049cdb0e.jpg",
                "https://i.pinimg.com/736x/69/fd/e0/69fde0df2c46727ae1169147b76cf902.jpg",
                "https://i.pinimg.com/736x/11/78/3e/11783ef48ca3d61097b562454f72667d.jpg",
                "https://i.pinimg.com/736x/c5/fb/2b/c5fb2b6a73c5452e42e98a7cd21b4afc.jpg",
                "https://i.pinimg.com/736x/d0/12/c5/d012c5440cc072e65a6216e5898f43f6.jpg",
                "https://postfiles.pstatic.net/MjAyNTAzMjRfOTcg/MDAxNzQyNzc1MjEyNzYx.cXU70An9vvx-hKsAnYUOa6rYtXP_XRoRKOyLlua9r7kg.JRUs3uuA1x-OF-kLvS-cP7rrLOHqPHhGnB_IUYGUoI4g.JPEG/IMG_5255.JPG?type=w966"]
    select_photo = random.choice(photo_url)
    await update.message.reply_photo(photo=select_photo, caption ="사쿠야 사진이 도착했습니다‼️📩")

async def send_ryo(update, context):
    photo_url = ["https://i.pinimg.com/736x/42/14/92/4214925b52424edfdb7a66e9dddfa414.jpg",
                "https://i.pinimg.com/736x/1d/0d/d4/1d0dd45ecc0ab5fa8a8dae3918b76962.jpg",
                "https://i.pinimg.com/736x/9e/1b/e9/9e1be984e813efa213f1fdf2bc1f408d.jpg",
                "https://i.pinimg.com/736x/13/32/ce/1332cef5fe4e10ab6b93655990ec30e8.jpg",
                "https://i.pinimg.com/736x/1d/b4/9d/1db49d52429280d0c85f33da4deb1785.jpg",
                "https://i.pinimg.com/736x/b4/61/88/b4618874e8dba5f418761535ea160ffe.jpg",
                "https://i.pinimg.com/736x/21/8f/d2/218fd258569c26e5d5b9b5db0e2f31c8.jpg",
                "https://i.pinimg.com/736x/6b/22/61/6b2261a6687ac14eb31b76e8c4435079.jpg",
                "https://i.pinimg.com/736x/5b/94/21/5b942158bf68588ed5b79a99b16cdb81.jpg",
                "https://i.pinimg.com/736x/54/72/fd/5472fdc6f8f2fea1b5b393c3c2ac7a6f.jpg",
                "https://i.pinimg.com/736x/c1/ad/9a/c1ad9a8b6f2b4f2de56df7f664769142.jpg",
                "https://i.pinimg.com/736x/3f/7a/67/3f7a67f5922f42f186de1b5321a022ed.jpg",
                "https://i.pinimg.com/736x/f1/1e/d0/f11ed0fb24cb390e343a65d0934599a8.jpg",
                "https://i.pinimg.com/736x/e1/15/24/e115249ec7e43d32bb32ce88e0d4b06a.jpg",
                "https://i.pinimg.com/736x/60/89/34/6089348f604ac776e7b7842f618486b4.jpg"]
    select_photo = random.choice(photo_url)
    await update.message.reply_photo(photo=select_photo, caption ="료 사진이 도착했습니다‼️📩")

async def send_jaehee(update, context):
    photo_url = ["https://i.pinimg.com/736x/53/61/d7/5361d7078ec1b330607c52bd5cd2c221.jpg",
                "https://i.pinimg.com/736x/e1/47/e8/e147e86cd19d566724d6d96a6ae7afa4.jpg",
                "https://i.pinimg.com/736x/a3/6b/bb/a36bbbb360edcdc08f06c06a68cd9772.jpg",
                "https://i.pinimg.com/736x/7b/ad/b1/7badb1dfd42ad91e2b00847674c092e1.jpg"]
    select_photo = random.choice(photo_url)
    await update.message.reply_photo(photo=select_photo, caption ="대영 사진이 도착했습니다‼️📩")