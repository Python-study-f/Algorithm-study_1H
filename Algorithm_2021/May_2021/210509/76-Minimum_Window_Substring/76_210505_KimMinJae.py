# try 2: clean dfs 224/ 266 TLE
class Solution:
    def __init__(self):
        self.mn=1e9
        self.ans=[0,0]
        self.dic=[[]for _ in range((ord('z')+1))]
        self.stock=[0]*(ord('z')+1)
        self.candi= []
        self.ed=0
        
    def clean_dfs(self,i,lo,hi):
        
        if hi-lo>=self.mn:
            return
        if i==self.ed:
            print(hi,lo)
            if hi-lo<self.mn:
                self.mn= hi-lo
                self.ans=[lo,hi]
            return

            #print(candi)
        
        self.candi[i].sort(key= lambda x: max(hi,x[2])-min(lo,x[1]))
        
        for _, nlo, nhi in self.candi[i]:
            nlo= min(lo, nlo)
            nhi= max(hi, nhi)
            if nhi-nlo>=self.mn:
                continue
            self.clean_dfs(i+1,nlo,nhi)


    def minWindow(self,s: str, t: str) -> str:

        n= len(s)
        m= len(t)

        for i in range(m):
            self.stock[ord(t[i])]+=1
        #print(stock)
        for i in range(n):
            if self.stock[ord(s[i])]:
                self.dic[ord(s[i])].append(i)

        for i in range(65, ord('z')+1):
            if self.stock[i]:
                self.candi.append([])
                if len(self.dic[i])-self.stock[i]+1<=0:
                    return ""
                for j in range(0,len(self.dic[i])-self.stock[i]+1):
                    ths= self.dic[i][j],self.dic[i][j+self.stock[i]-1]
                    nlo= ths[0]
                    nhi= ths[-1]
                    self.candi[-1].append((nhi-nlo, nlo, nhi))
        self.ed= len(self.candi)
        self.candi.sort(key= lambda x: len(x))
        #[print(len(el)) for el in self.candi]
        print(self.candi)
        self.clean_dfs(0,int(1e5),0)
        #print(n,m,self.ans)

        return s[self.ans[0]:self.ans[1]+1]


tst= Solution()
print(tst.minWindow("wegdtzwabazduwwdysdetrrctotpcepalxdewzezbfewbabbseinxbqqplitpxtcwwhuyntbtzxwzyaufihclztckdwccpeyonumbpnuonsnnsjscrvpsqsftohvfnvtbphcgxyumqjzltspmphefzjypsvugqqjhzlnylhkdqmolggxvneaopadivzqnpzurmhpxqcaiqruwztroxtcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanllpunlyohwfsssiazeixhebipfcdqdrcqiwftutcrbxjthlulvttcvdtaiwqlnsdvqkrngvghupcbcwnaqiclnvnvtfihylcqwvderjllannflchdklqxidvbjdijrnbpkftbqgpttcagghkqucpcgmfrqqajdbynitrbzgwukyaqhmibpzfxmkoeaqnftnvegohfudbgbbyiqglhhqevcszdkokdbhjjvqqrvrxyvvgldtuljygmsircydhalrlgjeyfvxdstmfyhzjrxsfpcytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmojsbaehupiocnmenbcxjwujimthjtvvhenkettylcoppdveeycpuybekulvpgqzmgjrbdrmficwlxarxegrejvrejmvrfuenexojqdqyfmjeoacvjvzsrqycfuvmozzuypfpsvnzjxeazgvibubunzyuvugmvhguyojrlysvxwxxesfioiebidxdzfpumyon","ozgzyywxvtublcl"))


#print(tst.minWindow("qxsncfwvbslazxuoxnedkukropehlwfbwxqycntdfgghecvdqbhcwtukkauwzzzvystcfohmupvastekunmqiidtjxriyqdyiyapohekxblrurbpgphoykjhjarhtwfduhvkpzumahdxagmivtxvgiepjvxetehnmczddurgdwdecrmzklxqubgfzfjslqizvheadvghrlnvcbxpnuhjxpqywzrkrbjokqpolxxflkapnzeatmltdbrackkwlvmwlbmxbjcmvebieilzwyszckzgulcihpgsssrtdvhaaligvvfrwaqyksegdjqmywfsoyotuxtwieefbjwxjpxvhcemnwzntgfjetdatyydecjgofdzudxbfbqsxpfsvmebijcbhcemfnuvtzupcrthujbuyiovvswdbagjdkxkyrftqbktvdcpogloqajlsgquiyfljcxjveengogbulsitexjeixwqpszoxkzzkiuooiweqxydqjywiiaqhyhwrgkosloetktjuponposfxrdhzdyibhesprjjczoyjhhgyxtnmlulextdatnecsyrlhangonsxxywutligguldpqgiemkymdjufycumwtjupfpdowjkjozzwjdivbvymrdlvzzstkmkpenfcyplnqkjzquutrsgiytdxsvsckftquzstqdihnrgfnbbevjovcutupnyburrpsjijmsqclyjzzk","fxtusxonrfdrhxjamdkwm"))


# try 1: dfs 234/266 TLE
class Solution:
    def __init__(self):
        self.mn=1e9
        self.ans=[0,0]
        self.dic=[[]for _ in range((ord('z')+1))]
        self.stock=[0]*(ord('z')+1)
        
    def dfs(self,i,lo,hi):
        if i==ord('z')+1:
            if hi-lo<self.mn:
                self.mn= hi-lo
                self.ans=[lo,hi]
            return
        if self.stock[i]:
            if len(self.dic[i])-self.stock[i]+1<=0:
                self.mn=-1
                self.ans=[0,-1]
                return
            candi=[]
            for j in range(0,len(self.dic[i])-self.stock[i]+1):
                ths= self.dic[i][j],self.dic[i][j+self.stock[i]-1]
                nlo= min(lo, ths[0])
                nhi= max(hi, ths[-1])
                candi.append((nhi-nlo, nlo, nhi))
            candi.sort()
            for _, nlo, nhi in candi:
                if nhi-nlo>=self.mn:
                    continue
                self.dfs(i+1,nlo,nhi)

        else:
            self.dfs(i+1, lo, hi)


    def minWindow(self,s: str, t: str) -> str:

        n= len(s)
        m= len(t)

        for i in range(m):
            self.stock[ord(t[i])]+=1
        #print(stock)
        for i in range(n):
            if self.stock[ord(s[i])]:
                self.dic[ord(s[i])].append(i)

        self.dfs(65,int(1e5),0)
        print(n,m,self.ans)

        return s[self.ans[0]:self.ans[1]+1]