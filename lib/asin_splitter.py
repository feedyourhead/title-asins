# -*- coding: utf-8 -*-

        # print asins
        # #to be moved to lib
        # asin_list = asins.split()
        # print asin_list

        # results = []

        # for asin in asin_list:
        #     item_trans = ItemTranslation().find_one_by_asin_and_sites(asins, src_site, dst_site)
        #     results.append(item_trans)
        # print results

        
        # return {'results': results, 'src_site':src_site, 'dst_site': dst_site}




# ts = TermSender()
#             terms = form.d.terms.splitlines()
#             userId = form.d.userID
#             # form.d.boe and form['boe'].value are equivalent ways of
#             # extracting the validated arguments from the form.
#             results = ""
#             for term in terms:
#                 result = ts.send_term(userId, term)
#                 results = "%s %s: %s <br>" % (results, term, result.content) 
#             return render.formtest(form, "send, result: <br>%s" % results)

# ${form.textarea("asin", cols="50", rows="10")}   