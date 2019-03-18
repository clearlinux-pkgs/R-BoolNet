#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-BoolNet
Version  : 2.1.4
Release  : 9
URL      : https://cran.r-project.org/src/contrib/BoolNet_2.1.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/BoolNet_2.1.4.tar.gz
Summary  : Construction, Simulation and Analysis of Boolean Networks
Group    : Development/Tools
License  : Artistic-2.0
Requires: R-BoolNet-lib = %{version}-%{release}
BuildRequires : R-XML
BuildRequires : R-igraph
BuildRequires : buildreq-R

%description
asynchronous, probabilistic and temporal Boolean networks, and to
        analyze and visualize attractors in Boolean networks.

%package lib
Summary: lib components for the R-BoolNet package.
Group: Libraries

%description lib
lib components for the R-BoolNet package.


%prep
%setup -q -c -n BoolNet

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552722116

%install
export SOURCE_DATE_EPOCH=1552722116
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BoolNet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BoolNet
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BoolNet
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  BoolNet || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/BoolNet/CITATION
/usr/lib64/R/library/BoolNet/DESCRIPTION
/usr/lib64/R/library/BoolNet/INDEX
/usr/lib64/R/library/BoolNet/Meta/Rd.rds
/usr/lib64/R/library/BoolNet/Meta/data.rds
/usr/lib64/R/library/BoolNet/Meta/features.rds
/usr/lib64/R/library/BoolNet/Meta/hsearch.rds
/usr/lib64/R/library/BoolNet/Meta/links.rds
/usr/lib64/R/library/BoolNet/Meta/nsInfo.rds
/usr/lib64/R/library/BoolNet/Meta/package.rds
/usr/lib64/R/library/BoolNet/Meta/vignette.rds
/usr/lib64/R/library/BoolNet/NAMESPACE
/usr/lib64/R/library/BoolNet/NEWS.Rd
/usr/lib64/R/library/BoolNet/R/BoolNet
/usr/lib64/R/library/BoolNet/R/BoolNet.rdb
/usr/lib64/R/library/BoolNet/R/BoolNet.rdx
/usr/lib64/R/library/BoolNet/data/cellcycle.rda
/usr/lib64/R/library/BoolNet/data/examplePBN.rda
/usr/lib64/R/library/BoolNet/data/igf.rda
/usr/lib64/R/library/BoolNet/data/yeastTimeSeries.rda
/usr/lib64/R/library/BoolNet/doc/BoolNet_package_vignette.R
/usr/lib64/R/library/BoolNet/doc/BoolNet_package_vignette.Snw
/usr/lib64/R/library/BoolNet/doc/BoolNet_package_vignette.pdf
/usr/lib64/R/library/BoolNet/doc/cellcycle.txt
/usr/lib64/R/library/BoolNet/doc/example.btp
/usr/lib64/R/library/BoolNet/doc/index.html
/usr/lib64/R/library/BoolNet/help/AnIndex
/usr/lib64/R/library/BoolNet/help/BoolNet.rdb
/usr/lib64/R/library/BoolNet/help/BoolNet.rdx
/usr/lib64/R/library/BoolNet/help/aliases.rds
/usr/lib64/R/library/BoolNet/help/paths.rds
/usr/lib64/R/library/BoolNet/html/00Index.html
/usr/lib64/R/library/BoolNet/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/BoolNet/libs/BoolNet.so
/usr/lib64/R/library/BoolNet/libs/BoolNet.so.avx2
/usr/lib64/R/library/BoolNet/libs/BoolNet.so.avx512
