__author__ = "https://github.com/thisismehdi"
__license__ = "GNU3"
__maintainer__ = "Mehdi"

import os
import sys
import Scripts.aparatApi as a
import Scripts.aparatLinksFinder as f


def main():
    ap = a.AparatDlApi()
    arg = sys.argv[:]
# HELP AND STUFF
    try:
        if arg.count("-H") or arg.count("--help"):
            print(
                '''
            Options:
                -H : Helps you =)
                -R :list all available qualities
                                       aparat_dl -R link
                -L  : Download whole play-list
                        aparat_dl -L link
                -SL : Download videos by selection on a play-list
                        aparat_dl  -SL start point endpoint link
                -F  : grabs links from a txt file
                         aprat_dl -F path/to/txt/file
                -LF : Download play-list from a txt File
                    aparat_dl -LF path/to/txt/file Note*:u can use -CR a long with it
                -CR : use with other flags first use -R to see the available resolutions
                        aparat_dl -CR 1080p -F/-L/-SL/-LF


            Notes:
                1.to download a single video use aparat dl link
                2.video /s will be downloaded as 720p by default !
                          to change it use flag -R to choose
                          the quality along with other
            '''
            )

        elif len(arg) == 1:
            print("""
				There is no link
                how to use :
                    Use help -H or --help to see how scripts work
                    aparat_dl -H

			""")
# LIST QUALITIES
        elif len(arg) == 3 and arg.count("-R"):
            if arg[-1].count("https://") or arg[-1].count("http://"):
                try:
                    print(f.reclister(arg[-1]))
                except Exception as e:
                    print(e)
            else:
                print("Get know how to use the  program with aparat_dl -h ")

# SINGLE VIDEO
        elif len(arg) == 2:
            if arg[-1].count("https://") or arg[-1].count("http://"):
                try:
                    ap.singleVideo(arg[-1])
                except Exception as e:
                    print(e)
            else:
                print("Get know how to use the  program with aparat_dl -h ")

        elif len(arg) == 4 and arg.count("-CR"):
            if arg[-1].count("https://") or arg[-1].count("http://"):
                try:
                    ap.singleVideo(arg[-1], arg[-2])
                except Exception as e:
                    print(e)
            else:
                print("Get know how to use the  program with aparat_dl -h ")
# LIST VIDEO
        elif len(arg) == 3 and arg.count("-L") or len(arg) == 3 and arg.count("-L"):
            if arg[-1].count("https://") or arg[-1].count("http://"):
                try:
                    ap.playList(arg[-1])
                except Exception as e:
                    print(e)
            else:
                print("Get know how to use the  program with aparat_dl -h ")

        elif len(arg) == 5 and arg.count("-CR") and arg.count("-L"):
            if arg[-1].count("https://") or arg[-1].count("http://"):
                try:
                    Numberofindex = arg.index('-CR') + 1
                    ap.playList(arg[-1], arg[Numberofindex])
                except Exception as e:
                    print(e)
            else:
                print("Get know how to use the  program with aparat_dl -h ")

# SELECET VIDEO
        elif len(arg) == 5 and arg.count("-SL"):
            if arg[-1].count("https://") or arg[-1].count("http://"):
                try:
                    if arg[-2] > arg[-3]:
                        ap.selectFromPlayList(
                            arg[-1], int(arg[-3]), int(arg[-2]))
                    else:
                        print("Get know how to use the  program with aparat_dl -h ")
                except Exception as e:
                    print(e)
            else:
                print("Get know how to use the  program with aparat_dl -h ")

        elif len(arg) == 7 and arg.count("-CR") and arg.count("-SL"):
            if arg[-1].count("https://") or arg[-1].count("http://"):
                try:

                    Numberofindexforcr = arg.index('-CR') + 1
                    Numberofindexforsl1 = arg.index('-SL') + 1
                    Numberofindexforsl2 = arg.index('-SL') + 2
                    if arg[Numberofindexforsl2] > arg[Numberofindexforsl1]:
                        ap.selectFromPlayList(
                            arg[-1], int(arg[Numberofindexforsl1]), int(
                                arg[Numberofindexforsl2]), arg[Numberofindexforcr]
                        )
                    else:
                        print("Get know how to use the  program with aparat_dl -h ")

                except Exception as e:
                    print(e)
            else:
                print("Get know how to use the  program with aparat_dl -h ")

# FILE VIDEO
        elif len(arg) == 3 and arg.count("-F"):
            if arg[-1].count(".txt"):
                try:
                    ap.fromFile(arg[-1])
                except Exception as e:
                    print(e)
            else:
                print("Get know how to use the  program with aparat_dl -h ")

        elif len(arg) == 5 and arg.count("-CR") and arg.count("-F"):
            if arg[-1].count(".txt"):
                try:
                    Numberofindex = arg.index('-CR') + 1
                    ap.fromFile(arg[-1], arg[Numberofindex])
                except Exception as e:
                    print(e)
            else:
                print("Get know how to use the  program with aparat_dl -h ")

# lIST FROM FILE
        elif len(arg) == 3 and arg.count("-LF"):
            if arg[-1].count(".txt"):
                try:
                    ap.fromFileForList(arg[-1])
                except Exception as e:
                    print(e)
            else:
                print("Get know how to use the  program with aparat_dl -h ")

        elif len(arg) == 5 and arg.count("-CR") and arg.count("-LF"):
            if arg[-1].count(".txt"):
                try:
                    Numberofindex = arg.index('-CR') + 1
                    ap.fromFileForList(arg[-1], arg[Numberofindex])
                except Exception as e:
                    print(e)
            else:
                print("Get know how to use the  program with aparat_dl -h ")

        else:
            print(
                """
                Use help -H or --help to see how scripts work
                python -m  aparat_dl.py arguments link
                or 
                aparat_dl arguments link
                """
            )
    except KeyboardInterrupt as e:
        print("\n you just killed the program mate ! ")
        sys.exit()

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
