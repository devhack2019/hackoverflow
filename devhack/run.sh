cd Images
for files in *
do
cd ..
i=$files
  echo $i
  python3 face_detect_cv3.py 'Images/'$i'/'$i'.jpg'
  cd SRN-Deblur-master
  python run_model.py --input_path='./../Images/'$i'/' --output_path='./../Images/'$i'/'
  cd ..
  python3 resize.py $i
cd Images
done
cd ..

cd Face\ Recognition
python3 siamese.py 
cd ..


