with open("gencode.v24.lncRNA_transcripts.fa", "r") as ins:
    lnc_fasta = ins.readlines()    # ins.readlines()[1:] if header
ins.close()

lnc_arr_n = []
lnc_arr_e = []
len_lnc = []


def padding_sequence_new(seq, max_len = 101, repkey = 'N'):
    seq_len = len(seq)
    new_seq = seq
    if seq_len < max_len:
        gap_len = max_len -seq_len
        new_seq = seq + repkey * gap_len
    return new_seq


for line in lnc_fasta:
    line = line.strip()
    if line.startswith(">"):
        temp = line.split("|")
        lnc_arr_e.append(temp[1])
        lnc_arr_n.append(temp[5])
    else:
        len_lnc.append(len(line))

print len(lnc_arr_e)
lnc_arr_e = set(lnc_arr_e)
print len(lnc_arr_e)

print len(lnc_arr_n)
lnc_arr_n = set(lnc_arr_n)
print len(lnc_arr_n)

out = open("lncRNA_length.txt", "w")

for line in len_lnc:
    out.write(str(line) + "\n")

    if train:
        if not ensemble:
            train_bags, train_labels = get_data(posi, nega, channel=channel, window_size=window_size)
            model = train_network(model_type, np.array(train_bags), np.array(train_labels), channel=channel,
                                  window_size=window_size + 6,
                                  model_file=model_file, batch_size=batch_size, n_epochs=n_epochs, num_filters=num_filters,
                                  motif=motif, motif_seqs=motif_seqs, motif_outdir=motif_outdir)
        else:
            print 'ensembling'
            train_bags, train_labels = get_data(posi, nega, channel=1, window_size=max_size)
            model = train_network(model_type, np.array(train_bags), np.array(train_labels), channel=1,
                                  window_size=max_size + 6,
                                  model_file=model_file + '.global', batch_size=batch_size, n_epochs=n_epochs,
                                  num_filters=num_filters, motif=motif, motif_seqs=motif_seqs, motif_outdir=motif_outdir)
            train_bags, train_labels = [], []
            train_bags, train_labels = get_data(posi, nega, channel=7, window_size=window_size)
            model = train_network(model_type, np.array(train_bags), np.array(train_labels), channel=7,
                                  window_size=window_size + 6,
                                  model_file=model_file + '.local', batch_size=batch_size, n_epochs=n_epochs,
                                  num_filters=num_filters, motif=motif, motif_seqs=motif_seqs, motif_outdir=motif_outdir)

            end_time = timeit.default_timer()
            print "Training final took: %.2f s" % (end_time - start_time)
    elif predict:
        fw = open(out_file, 'w')
        if not ensemble:
            X_test, X_labels = get_data(testfile, nega=None, channel=channel, window_size=window_size)
            predict = predict_network(model_type, np.array(X_test), channel=channel, window_size=window_size + 6,
                                      model_file=model_file, batch_size=batch_size, n_epochs=n_epochs,
                                      num_filters=num_filters)
        else:
            X_test, X_labels = get_data(testfile, nega=None, channel=1, window_size=max_size)
            predict1 = predict_network(model_type, np.array(X_test), channel=1, window_size=max_size + 6,
                                       model_file=model_file + '.global', batch_size=batch_size, n_epochs=n_epochs,
                                       num_filters=num_filters)
            X_test, X_labels = get_data(testfile, nega=None, channel=7, window_size=window_size)
            predict2 = predict_network(model_type, np.array(X_test), channel=7, window_size=window_size + 6,
                                       model_file=model_file + '.local', batch_size=batch_size, n_epochs=n_epochs,
                                       num_filters=num_filters)

            predict = (predict1 + predict2) / 2.0
        # pdb.set_trace()
        # auc = roc_auc_score(X_labels, predict)
        # print auc
        myprob = "\n".join(map(str, predict))
        fw.write(myprob)
        fw.close()
    else:
        print 'please specify that you want to train the mdoel or predict for your own sequences'