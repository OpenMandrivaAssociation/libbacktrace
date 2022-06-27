%define soname 0

%define git 20220406

Name:           libbacktrace
Version:        1.0.0
Release:        1.%{git}.1
Summary:        A C library that may be linked into a C/C++ program to produce symbolic backtraces
License:        BSD
Group:          System/Libraries
URL:            https://github.com/ianlancetaylor/libbacktrace
Source0:        https://github.com/ianlancetaylor/libbacktrace/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  libtool


%description
A C library that may be linked into a C/C++ program to produce symbolic backtraces
Initially written by Ian Lance Taylor iant@golang.org.
This is version 1.0. It is likely that this will always be version 1.0.
The libbacktrace library may be linked into a program or library and used to produce symbolic backtraces. 
Sample uses would be to print a detailed backtrace when an error occurs or to gather detailed profiling information. 
In general the functions provided by this library are async-signal-safe, meaning that they may be safely called from a signal handler.
The libbacktrace library is provided under a BSD license. See the source files for the exact license text.
The public functions are declared and documented in the header file backtrace.h, which should be #include'd by a user of the library.
Building libbacktrace will generate a file backtrace-supported.h, which a user of the library may use to determine whether backtraces will work. 
See the source file backtrace-supported.h.in for the macros that it defines.
As of October 2020, libbacktrace supports ELF, PE/COFF, Mach-O, and XCOFF executables with DWARF debugging information. 
In other words, it supports GNU/Linux, *BSD, macOS, Windows, and AIX. 
The library is written to make it straightforward to add support for other object file and debugging formats.
The library relies on the C++ unwind API defined at https://itanium-cxx-abi.github.io/cxx-abi/abi-eh.html This API is provided by GCC and clang.

%package -n %{name}%{soname}
Summary:        Backtrace C library
Group:          System/Libraries

%description -n %{name}%{soname}
This is a C library that may be linked into a C/C++ program to produce symbolic backtraces.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for developing applications that use %{name}.

%prep
%setup -q

%build
%{_bindir}/autoreconf -fi
%configure --disable-static --enable-shared --enable-silent-rules
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec %{__rm} -f {} ';'

%files -n %{name}%{soname}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/*.so
%doc README.md
%license LICENSE
