# -*- coding: utf-8 -*-
# 2018-09-23
# Limpia HTML generado por Word, para poder usarlo posteriormente en armado de plantilla html+campos formulario (gravity forms)
# Repo: wichert / htmllaundry
import io
from htmllaundry import sanitize
from htmllaundry.cleaners import CommentCleaner

nameFile = "Contrato de arrendamiento v.2.html"
fi = io.open(nameFile, mode="r", encoding="utf-8")
fo = io.open(nameFile + '-output.html', mode="w", encoding="utf-8")

#print LineCleaner

#cleanedHtml = sanitize(fi.read())
cleanedHtml = sanitize(fi.read(), cleaner=CommentCleaner)
fo.write(cleanedHtml)

fo.close()
fo.close()

print cleanedHtmlx
#programPause = raw_input("Press the <ENTER> key to continue...")
