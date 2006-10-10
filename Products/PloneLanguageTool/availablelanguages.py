# -*- coding: UTF-8 -*-

"""
   This file contains a list of language and country names.

   >>> languages == getLanguages()
   True
   
   >>> len(languages) == len(getNativeLanguageNames())
   True

   >>> combined == getCombined()
   True

   >>> len(combined) == len(getCombinedLanguageNames())
   True

   >>> len(countries) == len(getCountries())
   True
"""

def getLanguages():
    """ Get all languages"""
    return languages.copy()

def getNativeLanguageNames():
    """ Get all native language names"""
    native_languages = {}
    for lc in languages:
        native_languages[lc] = languages.get(lc).get('native')
    return native_languages

def getCombined():
    """ Get all combined languages"""
    return combined.copy()

def getCombinedLanguageNames():
    """ Get all combined language names"""
    combined_languages = {}
    for lc in combined:
        combined_languages[lc] = combined.get(lc).get('english')
    return combined_languages

def getCountries():
    """ Get all countries"""
    return countries

# This is a dictionary of dictonaries:
#
# 'langcode-variation' : {native : 'Native name', english : 'English name', flag : 'flag-*.gif'}
#
# The current structure is to have language codes following ISO639-1 and to
# have flags which are named according to country codes following ISO3166-1.
#

languages = {
'aa' : {'native' : 'магIарул мацI', 'english' : 'Afar', 'flag' : 'flag-dj.gif'},
'ab' : {'native' : 'бызшәа', 'english' : 'Abkhazian', 'flag' : 'flag-ge.gif'},
'af' : {'native' : 'Afrikaans', 'english' : 'Afrikaans', 'flag' : 'flag-za.gif'},
'am' : {'native' : 'አማርኛ', 'english' : 'Amharic', 'flag' : 'flag-et.gif'},
'ar' : {'native' : 'العربية', 'english' : 'Arabic', 'flag' : 'flag-ly.gif'},
'as' : {'native' : 'অসমিয়া', 'english' : 'Assamese'},
'ay' : {'native' : 'Aymara', 'english' : 'Aymara', 'flag' : 'flag-bo.gif'},
'az' : {'native' : 'Azəri Türkçəsi', 'english' : 'Azerbaijani', 'flag' : 'flag-az.gif'},
'ba' : {'native' : 'Bashkir', 'english' : 'Bashkir'},
'be' : {'native' : 'Беларускі', 'english' : 'Belarussian', 'flag' : 'flag-by.gif'},
'bg' : {'native' : 'Български', 'english' : 'Bulgarian', 'flag' : 'flag-bg.gif'},
'bh' : {'native' : 'Bihari', 'english' : 'Bihari'},
'bi' : {'native' : 'Bislama', 'english' : 'Bislama', 'flag' : 'flag-vu.gif'},
'bn' : {'native' : 'বাংলা', 'english' : 'Bengali'},
'bo' : {'native' : 'བོད་སྐད་', 'english' : 'Tibetan'},
'bs' : {'native' : 'Bosanski', 'english' : 'Bosnian', 'flag' : 'flag-ba.gif'},
'br' : {'native' : 'Brezhoneg', 'english' : 'Breton'},
'ca' : {'native' : 'Català', 'english' : 'Catalan', 'flag' : 'flag-cat.gif'},
'co' : {'native' : 'Corsu', 'english' : 'Corsican'},
'cs' : {'native' : 'Čeština', 'english' : 'Czech', 'flag' : 'flag-cz.gif'},
'cy' : {'native' : 'Cymraeg', 'english' : 'Welsh', 'flag' : 'flag-cym.gif'},
'da' : {'native' : 'Dansk', 'english' : 'Danish', 'flag' : 'flag-dk.gif'},
'de' : {'native' : 'Deutsch', 'english' : 'German', 'flag' : 'flag-de.gif'},
'dz' : {'native' : 'རྫོང་ཁ', 'english' : 'Bhutani', 'flag' : 'flag-bt.gif'},
'el' : {'native' : 'Ελληνικά', 'english' : 'Greek', 'flag' : 'flag-gr.gif'},
'en' : {'native' : 'English', 'english' : 'English', 'flag' : 'flag-gb.gif'},
'eo' : {'native' : 'Esperanto', 'english' : 'Esperanto', 'flag' : 'flag-eo.gif'},
'es' : {'native' : 'Español', 'english' : 'Spanish', 'flag' : 'flag-es.gif'},
'et' : {'native' : 'Eesti', 'english' : 'Estonian', 'flag' : 'flag-ee.gif'},
'eu' : {'native' : 'Euskara', 'english' : 'Basque', 'flag' : 'flag-eu.gif'},
'fa' : {'native' : 'فارسی', 'english' : 'Persian', 'flag' : 'flag-ir.gif'},
'fi' : {'native' : 'Suomi', 'english' : 'Finnish', 'flag' : 'flag-fi.gif'},
'fj' : {'native' : 'Fiji', 'english' : 'Fiji', 'flag' : 'flag-fj.gif'},
'fo' : {'native' : 'Føroyska', 'english' : 'Faroese', 'flag' : 'flag-fj.gif'},
'fr' : {'native' : 'Français', 'english' : 'French', 'flag' : 'flag-fr.gif'},
'fy' : {'native' : 'Frysk', 'english' : 'Frisian'},
'ga' : {'native' : 'Gaeilge', 'english' : 'Irish Gaelic', 'flag' : 'flag-ie.gif'},
'gd' : {'native' : 'Gàidhlig', 'english' : 'Scottish Gaelic'},
'gl' : {'native' : 'Galego', 'english' : 'Galician'},
'gn' : {'native' : 'Guarani', 'english' : 'Guarani', 'flag' : 'flag-py.gif'},
'gu' : {'native' : 'ગુજરાતી', 'english' : 'Gujarati'},
'gv' : {'native' : 'Gaelg', 'english' : 'Manx Gaelic'},
'ha' : {'native' : 'هَوُس', 'english' : 'Hausa'},
'he' : {'native' : 'עברית', 'english' : 'Hebrew', 'flag' : 'flag-il.gif'},
'hi' : {'native' : 'हिंदी', 'english' : 'Hindi', 'flag' : 'flag-in.gif'},
'hr' : {'native' : 'Hrvatski', 'english' : 'Croatian', 'flag' : 'flag-hr.gif'},
'hu' : {'native' : 'Magyar', 'english' : 'Hungarian', 'flag' : 'flag-hu.gif'},
'hy' : {'native' : 'Հայերէն', 'english' : 'Armenian', 'flag' : 'flag-am.gif'},
'ia' : {'native' : 'Interlingua', 'english' : 'Interlingua'},
'id' : {'native' : 'Bahasa Indonesia', 'english' : 'Indonesian', 'flag' : 'flag-id.gif'},
'ie' : {'native' : 'Interlingue', 'english' : 'Interlingue'},
'ik' : {'native' : 'Inupiak', 'english' : 'Inupiak'},
'is' : {'native' : 'Íslenska', 'english' : 'Icelandic', 'flag' : 'flag-is.gif'},
'it' : {'native' : 'Italiano', 'english' : 'Italian', 'flag' : 'flag-it.gif'},
'iu' : {'native' : 'ᐃᓄᒃᑎᑐᑦ', 'english' : 'Inuktitut', 'flag' : 'flag-it.gif'},
'ja' : {'native' : '日本語', 'english' : 'Japanese', 'flag' : 'flag-jp.gif'},
'jbo': {'native' : 'lojban', 'english' : 'Lojban'},
'jw' : {'native' : 'Basa Jawi', 'english' : 'Javanese', 'flag' : 'flag-id.gif'},
'ka' : {'native' : 'ქართული', 'english' : 'Georgian', 'flag' : 'flag-ge.gif'},
'kk' : {'native' : 'ﻗﺎﺯﺍﻗﺸﺎ', 'english' : 'Kazakh', 'flag' : 'flag-kz.gif'},
'kl' : {'native' : 'Greenlandic', 'english' : 'Greenlandic', 'flag' : 'flag-gl.gif'},
'km' : {'native' : 'ខ្មែរ', 'english' : 'Cambodian/Khmer', 'flag' : 'flag-kh.gif'},
'kn' : {'native' : 'ಕನ್ನಡ', 'english' : 'Kannada', 'flag' : 'flag-in.gif'},
'ko' : {'native' : '한국어', 'english' : 'Korean', 'flag' : 'flag-kr.gif'},
'ks' : {'native' : 'काऽशुर', 'english' : 'Kashmiri', 'flag' : 'flag-in.gif'},
'ku' : {'native' : 'Kurdí', 'english' : 'Kurdish'},
'kw' : {'native' : 'Kernewek', 'english' : 'Cornish', 'flag' : 'flag-con.gif'},
'ky' : {'native' : 'Кыргыз', 'english' : 'Kyrgyz'},
'la' : {'native' : 'Latin', 'english' : 'Latin', 'flag' : 'flag-va.gif'},
'lb' : {'native' : 'Lëtzebuergesch', 'english' : 'Luxemburgish', 'flag' : 'flag-lu.gif'},
'li' : {'native' : 'Limburgs', 'english' : 'Limburgish'},
'ln' : {'native' : 'Lingala', 'english' : 'Lingala'},
'lo' : {'native' : 'ພາສາລາວ', 'english' : 'Laotian', 'flag' : 'flag-la.gif'},
'lt' : {'native' : 'Lietuviskai', 'english' : 'Lithuanian', 'flag' : 'flag-lt.gif'},
'lv' : {'native' : 'Latviešu', 'english' : 'Latvian'},
'mg' : {'native' : 'Malagasy', 'english' : 'Madagascarian', 'flag' : 'flag-mg.gif'},
'mi' : {'native' : 'Maori', 'english' : 'Maori', 'flag' : 'flag-nz.gif'},
'mk' : {'native' : 'Македонски', 'english' : 'Macedonian', 'flag' : 'flag-mk.gif'},
'ml' : {'native' : 'മലയാളം', 'english' : 'Malayalam'},
'mn' : {'native' : 'Монгол', 'english' : 'Mongolian', 'flag' : 'flag-mn.gif'},
'mo' : {'native' : 'Moldavian', 'english' : 'Moldavian', 'flag' : 'flag-md.gif'},
'mr' : {'native' : 'मराठी', 'english' : 'Marathi'},
'ms' : {'native' : 'Bahasa Melayu', 'english' : 'Malay', 'flag' : 'flag-my.gif'},
'mt' : {'native' : 'Malti', 'english' : 'Maltese', 'flag' : 'flag-mt.gif'},
'my' : {'native' : 'Burmese', 'english' : 'Burmese', 'flag' : 'flag-my.gif'},
'na' : {'native' : 'Nauru', 'english' : 'Nauruan', 'flag' : 'flag-nr.gif'},
'ne' : {'native' : 'नेपाली', 'english' : 'Nepali'},
'nl' : {'native' : 'Nederlands', 'english' : 'Dutch', 'flag' : 'flag-nl.gif'},
'no' : {'native' : 'Norsk', 'english' : 'Norwegian', 'flag' : 'flag-no.gif'},
'nn' : {'native' : 'Nynorsk', 'english' : 'Norwegian Nynorsk', 'flag' : 'flag-no.gif'},
'oc' : {'native' : 'Languedoc', 'english' : 'Occitan', 'flag' : 'flag-fr.gif'},
'om' : {'native' : 'Oromo', 'english' : 'Oromo'},
'or' : {'native' : 'ଓଡ଼ିଆ', 'english' : 'Oriya'},
'pa' : {'native' : 'ਪੰਜਾਬੀ', 'english' : 'Punjabi'},
'pl' : {'native' : 'Polski', 'english' : 'Polish', 'flag' : 'flag-pl.gif'},
'ps' : {'native' : 'پښتو', 'english' : 'Pashto'},
'pt' : {'native' : 'Português', 'english' : 'Portuguese', 'flag' : 'flag-pt.gif'},
'qu' : {'native' : 'Quechua', 'english' : 'Quechua'},
'rm' : {'native' : 'Rhaeto-Romance', 'english' : ''},
'rn' : {'native' : 'Kirundi', 'english' : 'Kirundi'},
'ro' : {'native' : 'Română', 'english' : 'Romanian', 'flag' : 'flag-ro.gif'},
'ru' : {'native' : 'Русский', 'english' : 'Russian', 'flag' : 'flag-ru.gif'},
'rw' : {'native' : 'Kiyarwanda', 'english' : 'Kiyarwanda'},
'sa' : {'native' : 'संस्कृत', 'english' : 'Sanskrit', 'flag' : 'flag-in.gif'},
'sd' : {'native' : 'Sindhi', 'english' : 'Sindhi', 'flag' : 'flag-pk.gif'},
'se' : {'native' : 'Northern Sámi', 'english' : 'Northern Sámi'},
'sg' : {'native' : 'Sangho', 'english' : 'Sangho', 'flag' : 'flag-cf.gif'},
'sh' : {'native' : 'Serbo-Croatian', 'english' : 'Serbo-Croatian'},
'si' : {'native' : 'Singhalese', 'english' : 'Singhalese'},
'sk' : {'native' : 'Slovenčina', 'english' : 'Slovak', 'flag' : 'flag-sk.gif'},
'sl' : {'native' : 'Slovenščina', 'english' : 'Slovenian', 'flag' : 'flag-si.gif'},
'sm' : {'native' : 'Samoan', 'english' : 'Samoan'},
'sn' : {'native' : 'Shona', 'english' : 'Shona'},
'so' : {'native' : 'Somali', 'english' : 'Somali', 'flag' : 'flag-so.gif'},
'sq' : {'native' : 'Shqip', 'english' : 'Albanian', 'flag' : 'flag-al.gif'},
'sr' : {'native' : 'српски', 'english' : 'Serbian', 'flag' : 'flag-cs.gif'},
'ss' : {'native' : 'Siswati', 'english' : 'Siswati'},
'st' : {'native' : 'Sesotho', 'english' : 'Sesotho'},
'su' : {'native' : 'Sudanese', 'english' : 'Sudanese', 'flag' : 'flag-sd.gif'},
'sv' : {'native' : 'Svenska', 'english' : 'Swedish', 'flag' : 'flag-se.gif'},
'sw' : {'native' : 'Kiswahili', 'english' : 'Swahili'},
'ta' : {'native' : 'தமிழ', 'english' : 'Tamil'},
'te' : {'native' : 'తెలుగు', 'english' : 'Telugu'},
'tg' : {'native' : 'Тоҷики', 'english' : 'Tadjik', 'flag' : 'flag-tj.gif'},
'th' : {'native' : 'ไทย', 'english' : 'Thai', 'flag' : 'flag-th.gif'},
'ti' : {'native' : 'ትግርኛ', 'english' : 'Tigrinya'},
'tk' : {'native' : 'түркmенче', 'english' : 'Turkmen', 'flag' : 'flag-tm.gif'},
'tl' : {'native' : 'Tagalog', 'english' : 'Tagalog', 'flag' : 'flag-ph.gif'},
'tn' : {'native' : 'Setswana', 'english' : 'Setswana', 'flag' : 'flag-bw.gif'},
'to' : {'native' : 'Lea faka-Tonga', 'english' : 'Tongan'},
'tr' : {'native' : 'Türkçe', 'english' : 'Turkish', 'flag' : 'flag-tr.gif'},
'ts' : {'native' : 'Tsonga', 'english' : 'Tsonga'},
'tt' : {'native' : 'татарча', 'english' : 'Tatar'},
'tw' : {'native' : 'Twi', 'english' : 'Twi'},
'ug' : {'native' : 'Uigur', 'english' : 'Uigur'},
'uk' : {'native' : 'Українська', 'english' : 'Ukrainian', 'flag' : 'flag-ua.gif'},
'ur' : {'native' : 'اردو', 'english' : 'Urdu', 'flag' : 'flag-pk.gif'},
'uz' : {'native' : 'Ўзбекча', 'english' : 'Uzbek', 'flag' : 'flag-uz.gif'},
'vi' : {'native' : 'Tiếng Việt', 'english' : 'Vietnamese', 'flag' : 'flag-vn.gif'},
'vo' : {'native' : 'Volapük', 'english' : 'Volapük'},
'wa' : {'native' : 'Walon', 'english' : 'Walloon'},
'wo' : {'native' : 'Wolof', 'english' : 'Wolof'},
'xh' : {'native' : 'isiXhosa', 'english' : 'Xhosa', 'flag' : 'flag-za.gif'},
'yi' : {'native' : 'ײִדיש', 'english' : 'Yiddish', 'flag' : 'flag-il.gif'},
'yo' : {'native' : 'Yorùbá', 'english' : 'Yorouba'},
'za' : {'native' : 'Zhuang', 'english' : 'Zhuang'},
'zh' : {'native' : '中文', 'english' : 'Chinese', 'flag' : 'flag-cn.gif'},
'zu' : {'native' : 'isiZulu', 'english' : 'Zulu'}
}

combined = {
'ar-ae' : {'english' : 'Arabic (United Arab Emirates)', 'flag' : 'flag-ae.gif'},
'ar-bh' : {'english' : 'Arabic (Bahrain)', 'flag' : 'flag-bh.gif'},
'ar-dz' : {'english' : 'Arabic (Algeria)', 'flag' : 'flag-dz.gif'},
'ar-eg' : {'english' : 'Arabic (Egypt)', 'flag' : 'flag-eg.gif'},
'ar-il' : {'english' : 'Arabic (Israel)', 'flag' : 'flag-il.gif'},
'ar-iq' : {'english' : 'Arabic (Iraq)', 'flag' : 'flag-iq.gif'},
'ar-jo' : {'english' : 'Arabic (Jordan)', 'flag' : 'flag-jo.gif'},
'ar-kw' : {'english' : 'Arabic (Kuwait)', 'flag' : 'flag-kw.gif'},
'ar-lb' : {'english' : 'Arabic (Lebanon)', 'flag' : 'flag-lb.gif'},
'ar-ly' : {'english' : 'Arabic (Libya)', 'flag' : 'flag-ly.gif'},
'ar-ma' : {'english' : 'Arabic (Morocco)', 'flag' : 'flag-ma.gif'},
'ar-mr' : {'english' : 'Arabic (Mauritania)', 'flag' : 'flag-mr.gif'},
'ar-om' : {'english' : 'Arabic (Oman)', 'flag' : 'flag-om.gif'},
'ar-ps' : {'english' : 'Arabic (Palestinian West Bank and Gaza)'},
'ar-qa' : {'english' : 'Arabic (Qatar)', 'flag' : 'flag-qa.gif'},
'ar-sa' : {'english' : 'Arabic (Saudi Arabia)', 'flag' : 'flag-sa.gif'},
'ar-sd' : {'english' : 'Arabic (Sudan)', 'flag' : 'flag-sd.gif'},
'ar-so' : {'english' : 'Arabic (Somalia)', 'flag' : 'flag-so.gif'},
'ar-sy' : {'english' : 'Arabic (Syria)', 'flag' : 'flag-sy.gif'},
'ar-td' : {'english' : 'Arabic (Chad)', 'flag' : 'flag-td.gif'},
'ar-tn' : {'english' : 'Arabic (Tunisia)', 'flag' : 'flag-tn.gif'},
'ar-ye' : {'english' : 'Arabic (Yemen)', 'flag' : 'flag-ye.gif'},
'bn-bd' : {'english' : 'Bengali (Bangladesh)', 'flag' : 'flag-bd.gif'},
'bn-in' : {'english' : 'Bengali (India)', 'flag' : 'flag-in.gif'},
'bn-sg' : {'english' : 'Bengali (Singapore)', 'flag' : 'flag-sg.gif'},
'ch-gu' : {'english' : 'Chamorro (Guam)', 'flag' : 'flag-gu.gif'},
'ch-mp' : {'english' : 'Chamorro (Northern Mariana Islands)', 'flag' : 'flag-mp.gif'},
'da-dk' : {'english' : 'Danish (Denmark)', 'flag' : 'flag-dk.gif'},
'da-gl' : {'english' : 'Danish (Greenland)', 'flag' : 'flag-gl.gif'},
'de-at' : {'english' : 'German (Austria)', 'native' : 'Deutsch (Österreich)',  'flag' : 'flag-at.gif'},
'de-be' : {'english' : 'German (Belgium)', 'flag' : 'flag-be.gif'},
'de-ch' : {'english' : 'German (Switzerland)', 'flag' : 'flag-ch.gif'},
'de-de' : {'english' : 'German (Germany)', 'flag' : 'flag-de.gif'},
'de-dk' : {'english' : 'German (Denmark)', 'flag' : 'flag-dk.gif'},
'de-li' : {'english' : 'German (Liechtenstein)', 'flag' : 'flag-li.gif'},
'de-lu' : {'english' : 'German (Luxembourg)', 'flag' : 'flag-lu.gif'},
'el-cy' : {'english' : 'Greek (Cyprus)'},
'el-gr' : {'english' : 'Greek (Greece)', 'flag' : 'flag-gr.gif'},
'en-ag' : {'english' : 'English (Antigua and Barbuda)', 'flag' : 'flag-ag.gif'},
'en-ai' : {'english' : 'English (Anguilla)', 'flag' : 'flag-ai.gif'},
'en-as' : {'english' : 'English (American Samoa)', 'flag' : 'flag-as.gif'},
'en-au' : {'english' : 'English (Australia)', 'flag' : 'flag-au.gif'},
'en-bb' : {'english' : 'English (Barbados)', 'flag' : 'flag-bb.gif'},
'en-bm' : {'english' : 'English (Bermuda)', 'flag' : 'flag-bm.gif'},
'en-bn' : {'english' : 'English (Brunei)', 'flag' : 'flag-bn.gif'},
'en-bs' : {'english' : 'English (Bahamas)', 'flag' : 'flag-bs.gif'},
'en-bw' : {'english' : 'English (Botswana)', 'flag' : 'flag-bw.gif'},
'en-bz' : {'english' : 'English (Belize)', 'flag' : 'flag-bz.gif'},
'en-ca' : {'english' : 'English (Canada)', 'flag' : 'flag-ca.gif'},
'en-ck' : {'english' : 'English (Cook Islands)', 'flag' : 'flag-ck.gif'},
'en-cm' : {'english' : 'English (Cameroon)', 'flag' : 'flag-cm.gif'},
'en-dm' : {'english' : 'English (Dominica)', 'flag' : 'flag-dm.gif'},
'en-er' : {'english' : 'English (Eritrea)', 'flag' : 'flag-er.gif'},
'en-et' : {'english' : 'English (Ethiopia)', 'flag' : 'flag-et.gif'},
'en-fj' : {'english' : 'English (Fiji)', 'flag' : 'flag-fj.gif'},
'en-fk' : {'english' : 'English (Falkland Islands)', 'flag' : 'flag-fk.gif'},
'en-fm' : {'english' : 'English (Micronesia)', 'flag' : 'flag-fm.gif'},
'en-gb' : {'english' : 'English (United Kingdom)', 'flag' : 'flag-gb.gif'},
'en-gd' : {'english' : 'English (Grenada)', 'flag' : 'flag-gd.gif'},
'en-gh' : {'english' : 'English (Ghana)', 'flag' : 'flag-gh.gif'},
'en-gi' : {'english' : 'English (Gibraltar)', 'flag' : 'flag-gi.gif'},
'en-gm' : {'english' : 'English (Gambia)', 'flag' : 'flag-gm.gif'},
'en-gu' : {'english' : 'English (Guam)', 'flag' : 'flag-gu.gif'},
'en-gy' : {'english' : 'English (Guyana)', 'flag' : 'flag-gy.gif'},
'en-ie' : {'english' : 'English (Ireland)', 'flag' : 'flag-ie.gif'},
'en-il' : {'english' : 'English (Israel)', 'flag' : 'flag-il.gif'},
'en-io' : {'english' : 'English (British Indian Ocean Territory)', 'flag' : 'flag-io.gif'},
'en-jm' : {'english' : 'English (Jamaica)', 'flag' : 'flag-jm.gif'},
'en-ke' : {'english' : 'English (Kenya)', 'flag' : 'flag-ke.gif'},
'en-ki' : {'english' : 'English (Kiribati)', 'flag' : 'flag-ki.gif'},
'en-kn' : {'english' : 'English (St. Kitts-Nevis)', 'flag' : 'flag-kn.gif'},
'en-ky' : {'english' : 'English (Cayman Islands)', 'flag' : 'flag-ky.gif'},
'en-lc' : {'english' : 'English (St. Lucia)', 'flag' : 'flag-lc.gif'},
'en-lr' : {'english' : 'English (Liberia)', 'flag' : 'flag-lr.gif'},
'en-ls' : {'english' : 'English (Lesotho)', 'flag' : 'flag-ls.gif'},
'en-mp' : {'english' : 'English (Northern Mariana Islands)', 'flag' : 'flag-mp.gif'},
'en-ms' : {'english' : 'English (Montserrat)', 'flag' : 'flag-ms.gif'},
'en-mt' : {'english' : 'English (Malta)', 'flag' : 'flag-mt.gif'},
'en-mu' : {'english' : 'English (Mauritius)', 'flag' : 'flag-mu.gif'},
'en-mw' : {'english' : 'English (Malawi)', 'flag' : 'flag-mw.gif'},
'en-na' : {'english' : 'English (Namibia)', 'flag' : 'flag-na.gif'},
'en-nf' : {'english' : 'English (Norfolk Island)', 'flag' : 'flag-nf.gif'},
'en-ng' : {'english' : 'English (Nigeria)', 'flag' : 'flag-ng.gif'},
'en-nr' : {'english' : 'English (Nauru)', 'flag' : 'flag-nr.gif'},
'en-nu' : {'english' : 'English (Niue)', 'flag' : 'flag-nu.gif'},
'en-nz' : {'english' : 'English (New Zealand)', 'flag' : 'flag-nz.gif'},
'en-pg' : {'english' : 'English (Papua New Guinea)', 'flag' : 'flag-pg.gif'},
'en-ph' : {'english' : 'English (Philippines)', 'flag' : 'flag-ph.gif'},
'en-pk' : {'english' : 'English (Pakistan)', 'flag' : 'flag-pk.gif'},
'en-pn' : {'english' : 'English (Pitcairn)', 'flag' : 'flag-pn.gif'},
'en-pr' : {'english' : 'English (Puerto Rico)', 'flag' : 'flag-pr.gif'},
'en-pw' : {'english' : 'English (Palau)', 'flag' : 'flag-pw.gif'},
'en-rw' : {'english' : 'English (Rwanda)', 'flag' : 'flag-rw.gif'},
'en-sb' : {'english' : 'English (Solomon Islands)', 'flag' : 'flag-sb.gif'},
'en-sc' : {'english' : 'English (Seychelles)', 'flag' : 'flag-sc.gif'},
'en-sg' : {'english' : 'English (Singapore)', 'flag' : 'flag-sg.gif'},
'en-sh' : {'english' : 'English (St. Helena)', 'flag' : 'flag-sh.gif'},
'en-sl' : {'english' : 'English (Sierra Leone)', 'flag' : 'flag-sl.gif'},
'en-so' : {'english' : 'English (Somalia)', 'flag' : 'flag-so.gif'},
'en-sz' : {'english' : 'English (Swaziland)', 'flag' : 'flag-sz.gif'},
'en-tc' : {'english' : 'English (Turks and Caicos Islands)', 'flag' : 'flag-tc.gif'},
'en-tk' : {'english' : 'English (Tokelau)', 'flag' : 'flag-tk.gif'},
'en-to' : {'english' : 'English (Tonga)', 'flag' : 'flag-to.gif'},
'en-tt' : {'english' : 'English (Trinidad and Tobago)', 'flag' : 'flag-tt.gif'},
'en-ug' : {'english' : 'English (Uganda)', 'flag' : 'flag-ug.gif'},
'en-us' : {'english' : 'English (USA)', 'flag' : 'flag-us.gif'},
'en-vc' : {'english' : 'English (St. Vincent and the Grenadi)', 'flag' : 'flag-vc.gif'},
'en-vg' : {'english' : 'English (British Virgin Islands)', 'flag' : 'flag-vg.gif'},
'en-vi' : {'english' : 'English (U.S. Virgin Islands)', 'flag' : 'flag-vi.gif'},
'en-vu' : {'english' : 'English (Vanuatu)', 'flag' : 'flag-vu.gif'},
'en-ws' : {'english' : 'English (Western Samoa)', 'flag' : 'flag-ws.gif'},
'en-za' : {'english' : 'English (South Africa)', 'flag' : 'flag-za.gif'},
'en-zm' : {'english' : 'English (Zambia)', 'flag' : 'flag-zm.gif'},
'en-zw' : {'english' : 'English (Zimbabwe)', 'flag' : 'flag-zw.gif'},
'es-ar' : {'english' : 'Spanish (Argentina)', 'flag' : 'flag-ar.gif'},
'es-bo' : {'english' : 'Spanish (Bolivia)', 'flag' : 'flag-bo.gif'},
'es-cl' : {'english' : 'Spanish (Chile)', 'flag' : 'flag-cl.gif'},
'es-co' : {'english' : 'Spanish (Colombia)', 'flag' : 'flag-co.gif'},
'es-cr' : {'english' : 'Spanish (Costa Rica)', 'flag' : 'flag-cr.gif'},
'es-cu' : {'english' : 'Spanish (Cuba)', 'flag' : 'flag-cu.gif'},
'es-do' : {'english' : 'Spanish (Dominican Republic)', 'flag' : 'flag-do.gif'},
'es-ec' : {'english' : 'Spanish (Ecuador)', 'flag' : 'flag-ec.gif'},
'es-es' : {'english' : 'Spanish (Spain)', 'flag' : 'flag-es.gif'},
'es-gq' : {'english' : 'Spanish (Equatorial Guinea)', 'flag' : 'flag-gq.gif'},
'es-gt' : {'english' : 'Spanish (Guatemala)', 'flag' : 'flag-gt.gif'},
'es-hn' : {'english' : 'Spanish (Honduras)', 'flag' : 'flag-hn.gif'},
'es-mx' : {'english' : 'Spanish (Mexico)', 'flag' : 'flag-mx.gif'},
'es-ni' : {'english' : 'Spanish (Nicaragua)', 'flag' : 'flag-ni.gif'},
'es-pa' : {'english' : 'Spanish (Panama)', 'flag' : 'flag-pa.gif'},
'es-pe' : {'english' : 'Spanish (Peru)', 'flag' : 'flag-pe.gif'},
'es-pr' : {'english' : 'Spanish (Puerto Rico)', 'flag' : 'flag-pr.gif'},
'es-py' : {'english' : 'Spanish (Paraguay)', 'flag' : 'flag-py.gif'},
'es-sv' : {'english' : 'Spanish (El Salvador)', 'flag' : 'flag-sv.gif'},
'es-us' : {'english' : 'Spanish (USA)', 'flag' : 'flag-us.gif'},
'es-uy' : {'english' : 'Spanish (Uruguay)', 'flag' : 'flag-uy.gif'},
'es-ve' : {'english' : 'Spanish (Venezuela)', 'flag' : 'flag-ve.gif'},
'fr-ad' : {'english' : 'French (Andorra)', 'flag' : 'flag-as.gif'},
'fr-be' : {'english' : 'French (Belgium)', 'flag' : 'flag-be.gif'},
'fr-bf' : {'english' : 'French (Burkina Faso)', 'flag' : 'flag-bf.gif'},
'fr-bi' : {'english' : 'French (Burundi)', 'flag' : 'flag-bi.gif'},
'fr-bj' : {'english' : 'French (Benin)', 'flag' : 'flag-bj.gif'},
'fr-ca' : {'english' : 'French (Canada)', 'flag' : 'flag-ca.gif'},
'fr-cd' : {'english' : 'French (Democratic Republic of Congo)', 'flag' : 'flag-cd.gif'},
'fr-cf' : {'english' : 'French (Central African Republic)', 'flag' : 'flag-cf.gif'},
'fr-cg' : {'english' : 'French (Congo)', 'flag' : 'flag-cg.gif'},
'fr-ch' : {'english' : 'French (Switzerland)', 'flag' : 'flag-ch.gif'},
'fr-ci' : {'english' : 'French (Cote d\'Ivoire)', 'flag' : 'flag-ci.gif'},
'fr-cm' : {'english' : 'French (Cameroon)', 'flag' : 'flag-cm.gif'},
'fr-dj' : {'english' : 'French (Djibouti)', 'flag' : 'flag-dj.gif'},
'fr-fr' : {'english' : 'French (France)', 'flag' : 'flag-fr.gif'},
'fr-ga' : {'english' : 'French (Gabon)', 'flag' : 'flag-ga.gif'},
'fr-gb' : {'english' : 'French (United Kingdom)', 'flag' : 'flag-gb.gif'},
'fr-gf' : {'english' : 'French (French Guiana)', 'flag' : 'flag-gf.gif'},
'fr-gn' : {'english' : 'French (Guinea)', 'flag' : 'flag-gn.gif'},
'fr-gp' : {'english' : 'French (Guadeloupe)', 'flag' : 'flag-gp.gif'},
'fr-ht' : {'english' : 'French (Haiti)', 'flag' : 'flag-ht.gif'},
'fr-it' : {'english' : 'French (Italy)', 'flag' : 'flag-it.gif'},
'fr-km' : {'english' : 'French (Comoros Islands)', 'flag' : 'flag-km.gif'},
'fr-lb' : {'english' : 'French (Lebanon)', 'flag' : 'flag-lb.gif'},
'fr-lu' : {'english' : 'French (Luxembourg)', 'flag' : 'flag-lu.gif'},
'fr-mc' : {'english' : 'French (Monaco)', 'flag' : 'flag-mc.gif'},
'fr-mg' : {'english' : 'French (Madagascar)', 'flag' : 'flag-mg.gif'},
'fr-ml' : {'english' : 'French (Mali)', 'flag' : 'flag-ml.gif'},
'fr-mq' : {'english' : 'French (Martinique)', 'flag' : 'flag-mq.gif'},
'fr-nc' : {'english' : 'French (New Caledonia)', 'flag' : 'flag-nc.gif'},
'fr-pf' : {'english' : 'French (French Polynesia)', 'flag' : 'flag-pf.gif'},
'fr-pm' : {'english' : 'French (St. Pierre and Miquelon)', 'flag' : 'flag-pm.gif'},
'fr-re' : {'english' : 'French (Reunion)', 'flag' : 'flag-re.gif'},
'fr-rw' : {'english' : 'French (Rwanda)', 'flag' : 'flag-rw.gif'},
'fr-sc' : {'english' : 'French (Seychelles)', 'flag' : 'flag-sc.gif'},
'fr-td' : {'english' : 'French (Chad)', 'flag' : 'flag-td.gif'},
'fr-tg' : {'english' : 'French (Togo)', 'flag' : 'flag-tg.gif'},
'fr-vu' : {'english' : 'French (Vanuatu)', 'flag' : 'flag-vu.gif'},
'fr-wf' : {'english' : 'French (Wallis and Futuna)', 'flag' : 'flag-wf.gif'},
'fr-yt' : {'english' : 'French (Mayotte)', 'flag' : 'flag-yt.gif'},
'hr-ba' : {'english' : 'Croatian (Bosnia-Herzegovina)', 'flag' : 'flag-ba.gif'},
'hr-hr' : {'english' : 'Croatian (Croatia)', 'flag' : 'flag-hr.gif'},
'hu-hu' : {'english' : 'Hungarian (Hungary)', 'flag' : 'flag-hu.gif'},
'hu-si' : {'english' : 'Hungarian (Slovenia)', 'flag' : 'flag-si.gif'},
'it-ch' : {'english' : 'Italian (Switzerland)', 'flag' : 'flag-ch.gif'},
'it-hr' : {'english' : 'Italian (Croatia)', 'flag' : 'flag-hr.gif'},
'it-it' : {'english' : 'Italian (Italy)', 'flag' : 'flag-it.gif'},
'it-si' : {'english' : 'Italian (Slovenia)', 'flag' : 'flag-si.gif'},
'it-sm' : {'english' : 'Italian (San Marino)', 'flag' : 'flag-sm.gif'},
'ko-kp' : {'english' : 'Korean (Korea, North)', 'flag' : 'flag-kp.gif'},
'ko-kr' : {'english' : 'Korean (Korea, South)', 'flag' : 'flag-kr.gif'},
'ln-cd' : {'english' : 'Lingala (Democratic Republic of Congo)', 'flag' : 'flag-cd.gif'},
'ln-cg' : {'english' : 'Lingala (Congo)', 'flag' : 'flag-cg.gif'},
'ms-bn' : {'english' : 'Malay (Brunei)', 'flag' : 'flag-bn.gif'},
'ms-my' : {'english' : 'Malay (Malaysia)', 'flag' : 'flag-my.gif'},
'ms-sg' : {'english' : 'Malay (Singapore)', 'flag' : 'flag-sg.gif'},
'nl-an' : {'english' : 'Dutch (Netherlands Antilles)', 'flag' : 'flag-an.gif'},
'nl-aw' : {'english' : 'Dutch (Aruba)', 'flag' : 'flag-aw.gif'},
'nl-be' : {'english' : 'Dutch (Belgium)', 'flag' : 'flag-be.gif'},
'nl-nl' : {'english' : 'Dutch (Netherlands)', 'flag' : 'flag-nl.gif'},
'nl-sr' : {'english' : 'Dutch (Suriname)', 'flag' : 'flag-sr.gif'},
'pt-ao' : {'english' : 'Português (Angola)', 'flag' : 'flag-ao.gif'},
'pt-br' : {'native'  : 'Português (Brasil)', 'english' : 'Brazilian Portuguese', 'flag' : 'flag-br.gif'},
'pt-cv' : {'english' : 'Português (Ilhas Cabo Verde)', 'flag' : 'flag-cv.gif'},
'pt-gw' : {'english' : 'Português (Guiné-Bissau)', 'flag' : 'flag-gw.gif'},
'pt-mz' : {'english' : 'Português (Moçambique)', 'flag' : 'flag-mz.gif'},
'pt-pt' : {'english' : 'Português (Portugal)', 'flag' : 'flag-pt.gif'},
'pt-st' : {'english' : 'Português (São Tomé e Príncipe)', 'flag' : 'flag-st.gif'},
'sd-in' : {'english' : 'Sindhi (India)', 'flag' : 'flag-in.gif'},
'sd-pk' : {'english' : 'Sindhi (Pakistan)', 'flag' : 'flag-pk.gif'},
'sr-ba' : {'english' : 'Serbian (Bosnia-Herzegovina)', 'flag' : 'flag-ba.gif'},
'sr-yu' : {'english' : 'Serbian (Yugoslavia)', 'flag' : 'flag-yu.gif'},
'ss-sz' : {'english' : 'Swati (Swaziland)', 'flag' : 'flag-sz.gif'},
'ss-za' : {'english' : 'Swati (South Africa)', 'flag' : 'flag-za.gif'},
'sv-fi' : {'english' : 'Swedish (Finland)', 'flag' : 'flag-fi.gif'},
'sv-se' : {'english' : 'Swedish (Sweden)', 'flag' : 'flag-se.gif'},
'sw-ke' : {'english' : 'Swahili (Kenya)', 'flag' : 'flag-ke.gif'},
'sw-tz' : {'english' : 'Swahili (Tanzania)', 'flag' : 'flag-tz.gif'},
'ta-in' : {'english' : 'Tamil (India)', 'flag' : 'flag-in.gif'},
'ta-sg' : {'english' : 'Tamil (Singapore)', 'flag' : 'flag-sg.gif'},
'tn-bw' : {'english' : 'Tswana (Botswana)', 'flag' : 'flag-bw.gif'},
'tn-za' : {'english' : 'Tswana (South Africa)', 'flag' : 'flag-za.gif'},
'tr-bg' : {'english' : 'Turkish (Bulgaria)', 'flag' : 'flag-bg.gif'},
'tr-cy' : {'english' : 'Turkish (Cyprus)', 'flag' : 'flag-cy.gif'},
'tr-tr' : {'english' : 'Turkish (Turkey)', 'flag' : 'flag-tr.gif'},
'ur-in' : {'english' : 'Urdu (India)', 'flag' : 'flag-in.gif'},
'ur-pk' : {'english' : 'Urdu (Pakistan)', 'flag' : 'flag-ur.gif'},
'zh-cn' : {'english' : 'Chinese (China)', 'native' : '简体中文(中国)',  'flag' : 'flag-cn.gif'},
'zh-hk' : {'english' : 'Chinese (Hongkong)', 'native' : '繁體中文(香港)',  'flag' : 'flag-hk.gif'},
'zh-sg' : {'english' : 'Chinese (Singapore)', 'native' : '简体中文(新加坡)',  'flag' : 'flag-sg.gif'},
'zh-tw' : {'english' : 'Chinese (Taiwan)', 'native' : '繁體中文(臺灣)',  'flag' : 'flag-tw.gif'}
}

# countries list from http://alioth.debian.org/projects/pkg-isocodes/
countries = {
'AD':'Andorra',
'AE':'United Arab Emirates',
'AF':'Afghanistan',
'AG':'Antigua and Barbuda',
'AI':'Anguilla',
'AL':'Albania',
'AM':'Armenia',
'AN':'Netherlands Antilles',
'AO':'Angola',
'AQ':'Antarctica',
'AR':'Argentina',
'AS':'American Samoa',
'AT':'Austria',
'AU':'Australia',
'AW':'Aruba',
'AX':'Åland Islands',
'AZ':'Azerbaijan',
'BA':'Bosnia and Herzegovina',
'BB':'Barbados',
'BD':'Bangladesh',
'BE':'Belgium',
'BF':'Burkina Faso',
'BG':'Bulgaria',
'BH':'Bahrain',
'BI':'Burundi',
'BJ':'Benin',
'BM':'Bermuda',
'BN':'Brunei Darussalam',
'BO':'Bolivia',
'BR':'Brazil',
'BS':'Bahamas',
'BT':'Bhutan',
'BV':'Bouvet Island',
'BW':'Botswana',
'BY':'Belarus',
'BZ':'Belize',
'CA':'Canada',
'CC':'Cocos (Keeling) Islands',
'CD':'Congo, The Democratic Republic of',
'CF':'Central African Republic',
'CG':'Congo',
'CH':'Switzerland',
'CI':"Cote d'Ivoire",
'CK':'Cook Islands',
'CL':'Chile',
'CM':'Cameroon',
'CN':'China',
'CO':'Colombia',
'CR':'Costa Rica',
'CS':'Serbia and Montenegro',
'CU':'Cuba',
'CV':'Cape Verde',
'CX':'Christmas Island',
'CY':'Cyprus',
'CZ':'Czech Republic',
'DE':'Germany',
'DJ':'Djibouti',
'DK':'Denmark',
'DM':'Dominica',
'DO':'Dominican Republic',
'DZ':'Algeria',
'EC':'Ecuador',
'EE':'Estonia',
'EG':'Egypt',
'EH':'Western Sahara',
'ER':'Eritrea',
'ES':'Spain',
'ET':'Ethiopia',
'FI':'Finland',
'FJ':'Fiji',
'FK':'Falkland Islands (Malvinas)',
'FM':'Micronesia, Federated States of',
'FO':'Faroe Islands',
'FR':'France',
'GA':'Gabon',
'GB':'United Kingdom',
'GD':'Grenada',
'GE':'Georgia',
'GF':'French Guiana',
'GH':'Ghana',
'GI':'Gibraltar',
'GL':'Greenland',
'GM':'Gambia',
'GN':'Guinea',
'GP':'Guadeloupe',
'GQ':'Equatorial Guinea',
'GR':'Greece',
'GS':'South Georgia and the South Sandwich Islands',
'GT':'Guatemala',
'GU':'Guam',
'GW':'Guinea-Bissau',
'GY':'Guyana',
'HK':'Hong Kong',
'HM':'Heard Island and McDonald Islands',
'HN':'Honduras',
'HR':'Croatia',
'HT':'Haiti',
'HU':'Hungary',
'ID':'Indonesia',
'IE':'Ireland',
'IL':'Israel',
'IN':'India',
'IO':'British Indian Ocean Territory',
'IQ':'Iraq',
'IR':'Iran, Islamic Republic of',
'IS':'Iceland',
'IT':'Italy',
'JM':'Jamaica',
'JO':'Jordan',
'JP':'Japan',
'KE':'Kenya',
'KG':'Kyrgyzstan',
'KH':'Cambodia',
'KI':'Kiribati',
'KM':'Comoros',
'KN':'Saint Kitts and Nevis',
'KP':"Korea, Democratic People's Republic of",
'KR':'Korea, Republic of',
'KW':'Kuwait',
'KY':'Cayman Islands',
'KZ':'Kazakhstan',
'LA':"Lao People's Democratic Republic",
'LB':'Lebanon',
'LC':'Saint Lucia',
'LI':'Liechtenstein',
'LK':'Sri Lanka',
'LR':'Liberia',
'LS':'Lesotho',
'LT':'Lithuania',
'LU':'Luxembourg',
'LV':'Latvia',
'LY':'Libyan Arab Jamahiriya',
'MA':'Morocco',
'MC':'Monaco',
'MD':'Moldova, Republic of',
'MG':'Madagascar',
'MH':'Marshall Islands',
'MK':'Macedonia, the former Yugoslavian Republic of',
'ML':'Mali',
'MM':'Myanmar',
'MN':'Mongolia',
'MO':'Macao',
'MP':'Northern Mariana Islands',
'MQ':'Martinique',
'MR':'Mauritania',
'MS':'Montserrat',
'MT':'Malta',
'MU':'Mauritius',
'MV':'Maldives',
'MW':'Malawi',
'MX':'Mexico',
'MY':'Malaysia',
'MZ':'Mozambique',
'NA':'Namibia',
'NC':'New Caledonia',
'NE':'Niger',
'NF':'Norfolk Island',
'NG':'Nigeria',
'NI':'Nicaragua',
'NL':'Netherlands',
'NO':'Norway',
'NP':'Nepal',
'NR':'Nauru',
'NU':'Niue',
'NZ':'New Zealand',
'OM':'Oman',
'PA':'Panama',
'PE':'Peru',
'PF':'French Polynesia',
'PG':'Papua New Guinea',
'PH':'Philippines',
'PK':'Pakistan',
'PL':'Poland',
'PM':'Saint Pierre and Miquelon',
'PN':'Pitcairn',
'PR':'Puerto Rico',
'PS':'Palestinian Territory, occupied',
'PT':'Portugal',
'PW':'Palau',
'PY':'Paraguay',
'QA':'Qatar',
'RE':'Reunion',
'RO':'Romania',
'RU':'Russian Federation',
'RW':'Rwanda',
'SA':'Saudi Arabia',
'SB':'Solomon Islands',
'SC':'Seychelles',
'SD':'Sudan',
'SE':'Sweden',
'SG':'Singapore',
'SH':'Saint Helena',
'SI':'Slovenia',
'SJ':'Svalbard and Jan Mayen',
'SK':'Slovakia',
'SL':'Sierra Leone',
'SM':'San Marino',
'SN':'Senegal',
'SO':'Somalia',
'SR':'Suriname',
'ST':'Sao Tome and Principe',
'SV':'El Salvador',
'SY':'Syrian Arab Republic',
'SZ':'Swaziland',
'TC':'Turks and Caicos Islands',
'TD':'Chad',
'TF':'French Southern Territories',
'TG':'Togo',
'TH':'Thailand',
'TJ':'Tajikistan',
'TK':'Tokelau',
'TL':'Timor-Leste',
'TM':'Turkmenistan',
'TN':'Tunisia',
'TO':'Tonga',
'TR':'Turkey',
'TT':'Trinidad and Tobago',
'TV':'Tuvalu',
'TW':'Taiwan',
'TZ':'Tanzania, United Republic of',
'UA':'Ukraine',
'UG':'Uganda',
'UM':'United States Minor Outlying Islands',
'US':'United States',
'UY':'Uruguay',
'UZ':'Uzbekistan',
'VA':'Holy See (Vatican City State)',
'VC':'Saint Vincent and the Grenadines',
'VE':'Venezuela',
'VG':'Virgin Islands, British',
'VI':'Virgin Islands, U.S.',
'VN':'Viet Nam',
'VU':'Vanuatu',
'WF':'Wallis and Futuna',
'WS':'Samoa',
'YE':'Yemen',
'YT':'Mayotte',
'ZA':'South Africa',
'ZM':'Zambia',
'ZW':'Zimbabwe',
}

