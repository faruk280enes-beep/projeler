
while true
       sayi=input('oyuna başlamak için 1, oyunu bitirmek için -1 yazınız: ' ,'s');
       sayi=str2double(sayi) ;
       if isnan(sayi)
           disp('Geçersiz giriş. Lütfen -1 veya 1  giriniz.');
          
       
       elseif sayi==-1
          disp('Oyun sona erdi.');
        break

        elseif sayi==1
          toplam=0;
          while true
              while true
                  oyuncu1=input('Oyuncu1, 1 ile 10 arasında bir sayı giriniz: ','s');
                  oyuncu1=str2double(oyuncu1);

                  if isnan(oyuncu1)
                      disp('Geçersiz giriş. LÜtfen 1-10 arasında bir sayı giriniz')
                  elseif mod(oyuncu1,1)~=0
                     disp('lütfen 1 ile 10 arasında pozitif tam sayı giriniz');
                  elseif oyuncu1>0 && oyuncu1<11
                     toplam=toplam+oyuncu1;
                     break
                  else
                     disp(' Geçersiz giriş.');
                  end
              end
              if toplam>=100
                    disp('Tebrikler Oyuncu1, 100 sayısına ulaştınız')
                    break
              end
        
              while true    
                  oyuncu2=input('Oyuncu2, 1 ile 10 arasında bir sayı giriniz: ','s');
                  oyuncu2=str2double(oyuncu2);
                  
                  if isnan(oyuncu2);
                      disp('Geçersiz giriş. Lütfen 1-10 arasında bir sayı giriniz')
                  elseif mod(oyuncu2,1)~=0
                    disp('lütfen 1 ile 10 arasında pozitif tam sayı giriniz');
           
                  elseif oyuncu2>0 && oyuncu2<11
                     toplam=toplam+oyuncu2;
                     break
                  else
                    disp(' Geçersiz giriş. Lütfen 1 ile 10 arasında bir sayı giriniz.');
                  end
              end
              if toplam>=100
                    disp('Tebrikler Oyuncu2, 100 sayısına ulaştınız')
                    break
              end
    
          end
       else
            disp('lütfen 1 veya -1 değeri giriniz');
     
       end


end
