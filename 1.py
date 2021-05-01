def hitungVoucher(voucher,uangBelanja):
    DumbWaysJos = {'potongan':0.211,'minimal uang belanja':50000,'maksimal diskon':20000}
    DumbWaysMantap = {'potongan':0.3,'minimal uang belanja':80000,'maksimal diskon':40000}
    
    if voucher['potongan']*uangBelanja > voucher['maksimal diskon']:
        diskon = voucher['maksimal diskon']
    else:
        diskon = uangBelanja*voucher['potongan']
    bayar = uangBelanja - diskon
    kembalian = uangBelanja-bayar
    return print('Uang yang harus dibayar: ',int(bayar),'\nDiskon: ',int(diskon),'\nKembalian: ',int(kembalian))

hitungVoucher(DumbWaysMantap,100000)
