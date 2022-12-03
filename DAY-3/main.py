# Advent of Code DAY-3 by Pierrafrom in collaboration with Gayar

def divisioDeLigne(ligne):
    ligne1 = []
    ligne2 = []
    i = 0
    while i != len(ligne):
        if i < len(ligne) // 2:
            ligne1.append(ligne[i])
        elif i >= len(ligne) // 2:
            ligne2.append(ligne[i])
        i += 1
    listeDeLigne = [ligne1, ligne2]
    return listeDeLigne


def chercheCommun(listeDeLigne):
    ligne1 = listeDeLigne[0]
    ligne2 = listeDeLigne[1]
    mot = ''
    i = 0
    j = 0
    for i in ligne1:
        for j in ligne2:
            if i == j:
                mot = i
    return mot


#####################################################
def chercheNombre(charactere):
    chaine = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(chaine)):
        if chaine[i] == charactere:
            return i


#####################################################

def FinA(liste):
    nbFinal = 0
    for i in range(len(liste)):
        nbFinal += chercheNombre(chercheCommun(divisioDeLigne(liste[i])))
    return nbFinal


def tousLesChiffres(liste):
    mot = ''
    listeFin = []
    l = 0
    while l != len(liste):
        ligne1 = liste[l]
        ligne2 = liste[l + 1]
        ligne3 = liste[l + 2]
        for i in ligne1:
            for j in ligne2:
                for k in ligne3:
                    if i == j and i == k:
                        mot = i
        listeFin.append(chercheNombre(mot))
        l += 3
    return listeFin


def FinB(liste):
    nbFinal = 0
    for i in range(len(liste)):
        nbFinal += liste[i]
    return nbFinal

# file edited with Excel
Fichier = [
    "rZTmmqbBrmBvSTCwDDtlwjqnqnnq",
    "dhgQHhPfVgPlPdFzFzFgdptCQjtnwCntjsCppRtRND",
    "lVdVHWGPvTvmrrBW",
    "GmJBqwPLhfPBfJfvfffFmwtjDprpzVpVMpcDrVjzzcjpML",
    "HgWnRnWggWbNTWbCnPCgCnsjcVDrjMrdzjprMMrzcHDrDr",
    "SsSsRsCSPSPBvtJt",
    "BLtwwTBmLSTlMsjdZmFZZP",
    "hzbzNNrbqQbhQDDrhCprbhDCpvFJJPjMZJZgjjPdlvZjZvvl",
    "fbNrqrVDfdfGzqcHTBTVHwcTSHcH",
    "lcDdcrCDCRHJHBllPR",
    "tNGQwQhtzLhJBRHbPMBMjGBj",
    "NZZZpVqqFqpQpCTZcTnrTrnJJC",
    "BSNLNzbLLsMGSDLSsSBdVwTVQFdTVTtqgTwNVN",
    "lRjplvmWpgrqwlVFFr",
    "mfRCpWwvChZCBGSzZG",
    "mDSlGBGwhGhmLHCQnMMVMLMVFJ",
    "WTNfjNgzNdgNWfsgsWWcWgfrVrnnFHQbrHvFrVVdHMrnCr",
    "FpcggcNttFfqSqDtwBDmhZ",
    "HzNsHbGsddQHPrsNPNsTnNjMbjVbcVlMLjMjLtlttjjv",
    "CQfBZDQfWJlJlLJhvMMv",
    "WwwmWRfFwmCmwwzQzzzrdGNHFzNT",
    "JDvhJfdZZTdCTnmmTH",
    "qbPcsqbjcbstjbgnvqpRCBTCmgCm",
    "WPbPtbtVjWQsPvSVzSZLMDMVfLZJ",
    "NjMbTZPjHjbdBqNBqFqDFz",
    "LCcLSRLStRrLHShCtRfcpCtpQVqqDFDFqDdFpBddDQQFdB",
    "htCGtrSJLfScvwJvggbgwHgW",
    "hmPTmfFPwBFHhsBstJldltstVDSVrrpD",
    "CjzNGQjnRMMvMngMLGRVRBltVrVppqptVSqlVJ",
    "cLBjgjGGGCgvLLnhZThwcfTHPTcPmw",
    "SzwsVwcGsTVTmzmgjsLsmWWnGJZbbJbZtZqnDJntGq",
    "NHQvpvNRflHvQpPMlbtbZqbFDnWlqVrD",
    "dpPQVdpHMPRBpfCszCmsLsmcjdSg",
    "wZZGGrnGVvZGPTcTnGvVCVpmpJSgCJtNpWgWVgmC",
    "MdMRqqzMLDtQDQmzJg",
    "HBMdRLLBLBdbbBLHlRjLrHPPnTvGtTcwhGrhZtvh",
    "fcbcPWmvPvftWbDNVJJDrrhsJs",
    "wQvzqvpQQzHQwTTNVhrBGJTJ",
    "ZCMvzHMRCqggmWmndPngnn",
    "VjvVJvjdgjJNTVgdpjRttsTHSsbFqqRHSbBR",
    "nrfZLZCZnLnCCncZCrCQLSsFHHqtsSsSSBcHGtHsFh",
    "nQlLMrmwZtmwCMmMwZmtLLggvNvVjjNJglpDgzNdJJvN",
    "bCjQbTzCBlCvpqPTbZphtWWRhtddmDRRdRhPhh",
    "sLJsnJFcsnJcMMjNnfsjDDcDWcRgggtmwVRtVmhh",
    "sMsJLFfGrfFnrSNJjHzlTCCCQzpbBpzQzSBQ",
    "gWRzWwcrzWcgZHRzHmcpTLTgTLhQDSgFFLTpLD",
    "bBJfvJCssGJNjvPmbbmbLTQFTLQp",
    "jsCqBJsVsGBqCfNcWMmrRWlWqmwMcz",
    "cLjncLlQbllRhlnQTRblwtndsgpWdqgmnWNWmGpvWzdgzz",
    "DrFJBFFHZrrDDVJSNmpsWdzVpmzdqqzpzq",
    "FJPPHfDJPDPCZSZHFSDPCJtwRjClttNbwwjQLjcRhLlb",
    "tZZRtWCRtsspLRqSVqbPDfVvlfFDqV",
    "dgvMcccHHDHNrrbf",
    "wGwdgBBhhcBhCvTZvtCppp",
    "LRRNFfffFzzcrGRffNfcGNzJnrnhjdDMHHnrWdlmhddHnjrh",
    "BvStvwSqqCZVqtvpZBWMMhhFhWdmdMWMhm",
    "TTvqSbwqTPpZPzQsQRffsFGQ",
    "phZZpGbGVmqDbPTF",
    "tlNwlncnzwddcrGPlFmjlTTlfmjD",
    "zntnczBMdvBnnvnthHHZMJhCLpZSSRGQ",
    "ZwLLnbCDfClLZzZwDzCCZDbmNNdNtdBVNTNdNWMFtTFzTVFd",
    "vlPlJRgRhQcPQQjpcRQJBBthNdtddtthtFMNWqMq",
    "ppJgsgrJpJgslgrgRSPDDDLZLnHbrLHbwLbHfb",
    "sBrNSTsrgDDMSjpPWVVqhppbsbtz",
    "HTJfHwFwRFCnCPbzbzVzbVWq",
    "QTcvvcmHnwGvvnRNrLglNNLNDZcZZL",
    "qNNHSSFgbhLHHNfBwlJjQwwBcwQN",
    "WZnVrZrMpVvZmVjwBvzBQRflJJcz",
    "pWVGpWnmrmWjDmtnWVVZmtPFPCSbPgqgLSqtHCgTHgHH",
    "QcQHqhpqQGbvbqHNqfhsQfHczZMlBZdZBlSFFZpZlFMDRFBM",
    "TPVgmmrjtWjwrtwgLmTwLPMDZlMDMnSzzZgglzldBlgZ",
    "PVtPrmPddrPCVTNqcHvQbHsCQNGh",
    "PnsrrsdsSrnCvJCJBVwNqcHPRwNLWHwV",
    "pjTQlgGWMjZBbRHHHZcbVV",
    "htpThhlMjFdWrtDrfrsn",
    "GZjHFHgjpbZQbgpHdgpjjBMTQsMJWzWRcsLMCRWzcz",
    "ltwPlhwPSlwmmDhfrMwlzLLTSWJRssCBJWzsccCc",
    "nfrnrntPnDmDDnPrwmvlVGdGFFNqjVHNjbGFjgFNMp",
    "BjHBvHHqnBHrnnvclqjqplRRRQSfRpJQwPswStJsJQSt",
    "wVFGWdVZVhWVDzVdZDSfRJtLLZJPtJRJSfJP",
    "TDhCdWmNwzTWVmDBvMlrHmcqvHBMng",
    "HpDpHvjvCjDHZHVWJSCrnrJgnNwr",
    "rtQhssBTlRMblLBTtNnJFVSnnwVVwVWNnb",
    "BhrchlmBBszfjmzzffDf",
    "MMcJtJmVmnppVmSSpbCRvDvDRLDqvBRRCCMC",
    "GWNNGGGfrjlHHHNZZZLNZt",
    "jGrgfFjQrdhlhhgQFrVpnpVgmStPSJSPzJPP",
    "wvJNJNtfGGphQQjFdGWj",
    "DzSLzPczBrqzPrLMjSpjWMlSpQgwWd",
    "zPHRqBLqqHzPcBDPsznZCwJsnfVnmZmtVntC",
    "ttVWftWgGlWGfgtLtNddrNDdNvsLrdLdNm",
    "JCcFSnbBqbRbSBCBqTFSQCmwMjRsrDRNNjDddssNfDrr",
    "cBHBTTQFJJCCJQcCbCcqnSftHtZhHzWghPzVZpPglVVW",
    "ZfSGFQdbrHQSbFFqlwLjCjLPlqwj",
    "gmWJgNppJrgMcchzhmzNczqRsVRCjVRVsWjVRLRqqCVq",
    "zDTchzJJJhgJJmBJhBTJBggtQHGrdbfnHHDHGvftStvHdf",
    "LdRCgCDvCbCdnLnCvpGtQlhffNlhtSlQNtQlhb",
    "BTJTVFJrqMVmBmdTMFNHNVQQQSHHffQhNlHQ",
    "MqcBmqPdFBdjPPBTJqpZDDpgGDpgWCcvGCLp",
    "gzFbjgqljdqblbbddBZTMvTBdMsVvm",
    "SHpGWBCtSPhNpPSSSpwSNGNSTLTVVsZsLrvRrRvVLLRCvTvm",
    "NwhHwPhDtSGpbDcBQqczbBBj",
    "BhzLDSflLlTTRfqGpJZZQsqfNF",
    "ndCmMHHRPbCjCwVPVmjtwdMVsNGJQpZQsJqJqNJdFqJZFrNq",
    "CtwbRcRbttHBSgTcgShvTz",
    "pffmzCtppTSWtzdhbJdZvvHVnvdHVV",
    "WMlLWRGGQWMGrQJcVbvbHnvQHbhv",
    "LFwRFDlqFPWfTszp",
    "sbfFTbbbzJzfbJZSbnsnfTchGWWJGlhWvvBGltgVttgWgg",
    "LLLDpHwMDLmNjmChVWWBwthrGQvgQl",
    "dLMLDMLBNddPHmpMPfqPcPzcsSbbccqb",
    "MNGMPvHTnfTfgSFrSMMgwFMw",
    "QQRpjBsqhRQsldpqRQQQmjZFtrrzSFFccvSWwwjwFWZS",
    "smsBbQlRlmDpDBqpqblpLbLLfTfNVPVVGnTvTLbb",
    "gsmFlVCShjVwNNDNgWBNHg",
    "dMtQvtQRrtbLMqMnqqsq",
    "GQfGQPRtrPddPtvcvcQZRvRpJlVJFTlpZTVJpFJsSCFJjh",
    "LFmpcmhNfhhnjStshM",
    "qWTCCQrqlQBQcJCqrJdlHDdnRtngRStnPjgDSgSsjM",
    "CZWrqTbllrClJZWbVfmmZcvVzmGZmfpv",
    "qJLCqjwjjJnFqnDQQfqlQMfMQlMg",
    "zmHWPhGGZVGpcCWMsWRRfBBRDs",
    "bdpCcGmZdNFTwnSjrd",
    "TttqjWvQjZTtzwWtdBCMdBMqdGCBRnhR",
    "bpJlcNFVzbcBhCMMCChbMP",
    "cJVgrplDcslrlrpFzwTHQsSTWLQtjWvLWj",
    "hWlmVhlpcNpScSVtNbjrbGqdHGjgQrdrRdqG",
    "LPBDCvFszTCzFzFzBBffHrJrrGHRHsgRjsjrjJqc",
    "DTCMMzzvvnDvLvLDTTBTCMFBpWpthShmwmmWmwchptnhwWWt",
    "dfHqNQSQQNQBHHZJfJCMCfVcRJCZ",
    "GjLrDjgvFrFzjDgPGvLzgmmjCslRZMMCststJMlRcPVTRJJM",
    "vjmmvrnzDDLVzrdSWNBQnWwdhHhH",
    "jTmMBMNBTVSqNgBTjgNMqMTgWZttCmLfpQQZQWtLCdCGGtWC",
    "zzVVbhFcbzstWCZpsftsQZ",
    "whwhwPnDhHRhbRVHcSNllvMnNnjMjSBJMl",
    "nSvQgHWtZvHlgtvqgqngjSFFFDNSfsbbbjGfcsSr",
    "PPVRdNwRLhdLLCCwbscBBfGfbLjjjDbs",
    "zVPPhMhMmhhVppRpMNRPhMQnHqZtHZvgQzWgQgvnqnnq",
    "JdFHDSShfgDNMhGTBlwGGJqjjJTr",
    "PCnWnsvpzPnmLvmsQGRGWrwlWbljwTjFGl",
    "PtnLzQCQLfSFctdNhN",
    "cTrjrCNrLjTFCTrLCdSVNVlJVSVVGJftNp",
    "swQHQDsQGRZGffQV",
    "ggffMhhvgswDgDnhhfCcTjrcTjWBWCMmcjjc",
    "wGHvHCvWlMLlhGWwvvwlNnRBRdDNDBLDRVVDFdBD",
    "MtJJTPTTQNFRNFRfTn",
    "crSsmmJjmtgWmMhwWMCw",
    "sQQHWGsWcWWrZQQshNtHFNBCNBqHFwHB",
    "jSLbMSdfjSjFtFghNtFBMt",
    "RSdmtLmSLLzSLdjjdTTbVvsVVsvZcZQzWPWcQrrW",
    "PCCTzTgDgzVZZLgcgcdswMMMgs",
    "hSrqdqRQSjqtNqcsGWcGLwMGMf",
    "tlQJRJSRjpJjZPdpDTdHbzTn",
    "pqBGDDtQBDLVhfCtCZVV",
    "bTNFcljgbdlFjbldjFdTTcfZqZVsLhgfVLhVhZVHfZwC",
    "McJjFbvTWvmRqGRr",
    "JRcsJDfgncfHnqSBqGSTGQsTTz",
    "vlBlLlpNWpPhVmTQpQSzqbqQ",
    "CBPvjFNMlFhCCRtZJZZHfg",
    "RFQQTdQQLtThDhfRcHdLfFcHJCWtbbPnJWJPNJbnJsvstvJv",
    "ZmMlMlwwMrVzwVqrSqmZrqbplpNWFbWJnvvspWWNslNs",
    "gwwmFrgMGgFqGTHRhHjDRTHH",
    "dNfQvLdQsvSLsHsLBgNWVggJJCWCDJgnJJ",
    "ZTGcflFlFRfhbwhbPcbbbWVWrMVMnDJCCWmVnDJCmF",
    "lTfZTpjjZhPhRcqtBtsdSQpqQvtv",
    "frfccJzjTBwWwcJwjrwcBVCVTRCGnpsGGSmpVSSpDH",
    "hhhvghZvZlZvghPbdtqGpGVCRHGGmsRmpsvGRV",
    "MdPCNqdtgZdZgcWMLzcffBcWzM",
    "LdsfZNRsRWvvfLSsCpSgCDJbPcCp",
    "MqTVtHHThllGMthlBHzcSzGGSFppPgbJDFbF",
    "nVHwVlHmlhRWdjjjLvwD",
    "whhWFjjzhGmGCrFFFzvtZsLZVStNZWLNpvtv",
    "nqPMBdMQBqJnnfqdsSNfpvtZsSNtNpLp",
    "HJHnQHqQlhwLlhzmGh",
    "nMlmnfHmfjjmflLlLdzJTrsrBLJJLBbBSJrJ",
    "pZRpFFDWctFPNtWvbbrTqrszTbqbcBqr",
    "RpRGNPPvPFsNvflmdfwMGHhmmH",
    "PjPzphfpJFPvFRHDbP",
    "QlLlBcvBvnWCWcVCnFTTSnFDNdSRRRHN",
    "sVtlVcVtmqjMJphrfvJs",
    "dRRHRfrdRHHlCTTprlNCvhVVvhzpQhVvtmntmhtz",
    "JMDJBLwQMBDDwZgJnhSzhmWStMvzbbmm",
    "PPwJwGqPGQcDcHHjCqRlRCjrCN",
    "GgGgbGSGzGbMBBzGDVFbDMRpmcWWTTfcFTchsJdcWJchTsch",
    "NCqCttLZrCPQtNrtWqfhWJJqscmTJwsc",
    "ZClvLCLmPjnPllPvCLrmnDRjpDzGpMRDRRDBGBgSzb",
    "tvwCtDMQvJJPJtvQprjrjrvBjsTZTWTj",
    "gFzgldFZSlSbgFlZmGmcFqsppjsLqrBsLBrqqWWjdB",
    "FlcbhhNNbmHmcbSSzzggwDDQDwJnVCVHPtMVnnZQ",
    "hrCnnrFrCvFHzVFdmmFm",
    "GDTBsSfDDBRwfDsQbSdjHHVlqpmpgqWqpH",
    "TBDBDBQBwcsPsPGQswPcZvJMrJhnrNhrNNnHJM",
    "CztfzfZLBjMqZZWZgT",
    "VPcblQhJvtgbvbgb",
    "wwFQwVRPRchwcrJcPzfRpzspBfzfnSCzmt",
    "FMnmnQnFNdQFRtmFmfNsCsjfpfrHHfVffV",
    "DlLqDPwGlbVCdVbddbsr",
    "GPDzLhqwLqDMFdFJRWzQzd",
    "CSDSrMqnVSCTsPGPZpnPPGvP",
    "jhBhhqBQQlhgjthBhlhJpLlwLLPwsswsGZpWPLvP",
    "dgJQzgFjzjJFzzdHFzzzJMmNHCrSMSCSNbRqDCMCmR",
    "cvSPvzWwzcTbVWSPbppWVjsGjdHdQSlNsQSdNGqsHZ",
    "MRmCfmFBfRJfjqrdNMZHZQjQ",
    "qgFtChDCFgmCnppPnczPbcLpnL",
    "RllsdrhQvcVqmVzQcm",
    "gGgnrZZMrFWFpZcccVmHqjVmHHnJ",
    "ZrMWTTbbGMpbtgCTTZgZCWCLhwdsLvhhhPhNSldvPwPNfNlR",
    "ffMqqznPPMzHfdfcdBJGTMVTGjRmMMTBjr",
    "vtDwSwpmDsmQZswWSDhhDQGrjTgJBglRsjTTjVRBVTBl",
    "ZthhQStwppSSvbvNDtWwnnbffmPnHPFHqmzFbLFq",
    "CcHPmPcTJTqNCPqbqJqLgNJrjWtrftjrrnBnsWtjtBsfTB",
    "ZRLwhzwLRlhLpdlpjftBBnBjWsBBvn",
    "QhzhlwDdMzwFSwRLMJqqcSmqNPgmqNHNVP",
    "WzTWppwcQNppbQrJHhhrJfcdfnsr",
    "MDMLlLqjvqSBvVCLGJhnJsrDnnrDdhDffZ",
    "BLMCBCBlLlGSJvSPBMLqGJVwwQzPpNRWmTRzmzpWWFmTbQ",
    "WpWpWsfcBFjwGgqqtTQrTpgg",
    "JLHNPPvLJRZdnNJZHRzGGTzjrtMqMJlQzztt",
    "vHHnbDnLnHRCRnvdZdbHLNPfBfBhcffmcSSsDjcVwVBmcS",
    "DDZlblRRLQcNpJNhpL",
    "VPrdJfBFFBBWBrdvJPCBBdfhqcFhchNQcpNgzqcjphqFjp",
    "mWVPfMWWfBMWWwPrWvJHDbZGZmZRtDbsDbSb",
    "PDwwBzvRRzPCBPgnrwvvCDsSSccWscFTnSshWnZsSZcF",
    "GJtNGHfLbQtQQJQGhhhShgSZWVWJjSFF",
    "tmHlfGfMlBzrRDMggz",
    "gSBNwDNJglSwlDMtTCsZzStTsSCC",
    "hhfGdGcFhrqFmQddrhvvrdGRRtQMTHMCsbZbZtRTsbZsQs",
    "mrmrFqqqccdhWjGcnLpBDWgNWpCBlgLW",
    "WgmBsqMBnLLGnGnJtFgbbTwHttTwHF",
    "cQjcfpVQfCCPSMjCcCPSPjVwbtTlTtwJbTvJJHbzHFFJ",
    "PCZDCZffCdpQCdDWrGGsnLqWhnrM",
    "gppVszSgMPMPstzNpPMQpnGfDJhfnGLLGnfLfQlLfh",
    "rBFcCcrbmbJJJWhbhLVL",
    "wqcmRFZqmcvvCZBcRvcVwNsztSPzHstSgzMNSgpS",
    "qzLJRZfpRZtNNMSfftFN",
    "QDnPHCCGvbQnnCwMMlcFgsgHFFlNlV",
    "rPCMQnbdhRLqJLzhzB",
    "dfdrfqBqBtRwBsFR",
    "cDczzSMzDcSGSQbCfFjRFZtZCZmtwZRt",
    "bVcJSbVbSDllNrrWWNdvWf",
    "WSPPWlppCQlZPGqPjhcjfs",
    "JJrJrRTHNTNLbbNLcfzzSfSzGTjsqZsj",
    "FVRFNgVRbDbdwlWpSnvQnVQM",
    "znJTCRCSvRpzVBjWJdBBBVNb",
    "gggcfGDrGDZqwhwfGBjbHVSVdtdjtBShWj",
    "ZrgmqmGDGfDPmrfwPmsqZPfCpsFFnFvlSMCLLvpSRFFMvL",
    "qhhfgzzSGDSZSgfrcjhcjCCndnbjdr",
    "FPTTTwBHBPJMJVJBGwmjvCmBdjjNNcrjncNc",
    "GwTttMsTtHFtVFtDplSDzgRpDqsfpD",
    "vzwsPlvFFdJGjQwdJw",
    "HHNbpDTbVMvTpmMHvddtRtJJjjJRdLmLGj",
    "HbqHcbMvlWrqzWFW",
    "hMJMJBhPTnDMJJTGmmGmwDpRzRpFWz",
    "lSZPPNvbNllPpGRFwwzRNGgm",
    "bHZCZbvrttlZClqbHbsrbnQMThdJBQhVQBPdscnPQB",
    "ZRNZfffHLfDLgfNlHWwhChWzzVdcVH",
    "jpJmJjvnTtSjtJvQWldPWcBdPSdWzzcz",
    "jGGsGsFFFGnJtTvvTszZNqqNgrsDLRDqLqrL",
    "rrblpnfnVVfspgrppnMrpsrGdGdzgddzPFCjCzjzzzjtDC",
    "TRWTJwThJhRvwZWvJBZvqDzQzGBPCzdHGjdGGGttzj",
    "JSZmTZZwWvqhwqrrVnrLnPmbsbPr",
    "MdhjZhZZDTdPDcgCSLfgCpCL",
    "vvwtnwnssznwJnwvBbBBHHRSSfLLcpWfSWWzcLRTRWpf",
    "snJtHJHmbBsrswNtsnjhlhqZPqTjjTjQMPGr",
    "gmSnWMMzvvNWCNWCJJph",
    "QfqjcbcRGGjcwhNppNqMptdNHL",
    "rGPbflPfwPvlFFvTTMlg",
    "trTdMJvtlLntbCRN",
    "GBZsGFGBcRbZCRNR",
    "SSGFmFjqVNFVssjSVjqjvMMQvgTmMgMMQWMmTdhJ",
    "GcNcdNdwMZSqNZSSScSdqGwDrCmJMVrCmHmVVCFVJDrmFV",
    "jTvsRsWbjjbQQfvTThFVZVTVDJVHlCFr",
    "BjnBPfRWBnRsnvBsRBQQSSGzpZLdgwcLZqzgzPLg",
    "clNrNpjbNpbRrCpsRlrVtjwVZwttttZVgMHwZS",
    "FJBBDhJDTQFThqssvPJBBvHMWLwgwSHtWLZMwZgwSg",
    "qQJfdJDhGsBBDFJBnlzGmmnRzbCpcrzl",
    "ZPbfgBvcZPPZPWWWWBFbQllndnqdnlpwdSNfnwdN",
    "LzLrzDhmDRRJpJzptDhCSCqHMHqnqSlHqMSQNHQS",
    "zTsRzsDTJszzrrLRstrGJLsPpbVVPbcgTBcZvbPVFggbjP",
    "THpVHSrLZrzzvPtJdtsqLssdLW",
    "fbfCCQgQllWwwwFmjRsPcqcPsJJJdscPdmsP",
    "RNQlQgCFfgwVppWTNvGrvn",
    "PqFwwcqzDlFJDDQVMjQmMBjG",
    "ZgTZZndCpBMVNTvvQc",
    "pHgtZdtRnnLhcshdhWzWSFlbsJsqzzzbSb",
    "zjfgjMhhgMJdfHQHWdVQvR",
    "CrmpmpZpHQptHHHQ",
    "CnwcFbNCqQBFwwFFsPslJgsjhMlMcDJP",
    "HpnStLpnQnHnqQLQqpMSSWWZbswNcNqwbNsfwqGGZc",
    "dVRRTCTVJNLcfJcJFb",
    "gzjTRCddgLDdzdjCCrBjjdhhBnQPSSBhvlSBQvMhQMnt",
    "lFTlwMwZlblSjrCpVvvsptspZpps",
    "nHRPPnqnhPRqJHhqqhfdPqLCHvBCvvscvVNczztCCvsvtm",
    "RJDghDhRhhGPPqGhsPhhFSbbwGSFjGQlWTrbwQbW",
    "RRjgNPTRFhglgNNjTsmGqCCGZfzmHCnZGnZCqq",
    "SppWLbtbCzZMpHMZ",
    "dSDbbJdVVlHFNlll",
    "dtZdGmqqtmzhtqZtZswzSnSjfNHNVjzCWCnCffHz",
    "LgpMFMvlhvRMhhDDlvvQLFJCfSCHnFVJnSnJHNjSnj",
    "rRBLcQcpQcrZbwsZshbs"
]

Nombre1 = FinA(Fichier)
Nombre2 = FinB(tousLesChiffres(Fichier))
print(Nombre2)




