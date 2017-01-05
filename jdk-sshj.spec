Name     : jdk-sshj
Version  : 0.8.1
Release  : 1
URL      : http://repo.maven.apache.org/maven2/net/schmizz/sshj/0.8.1/sshj-0.8.1.jar
Source0  : http://repo.maven.apache.org/maven2/net/schmizz/sshj/0.8.1/sshj-0.8.1.jar
Source1  : http://repo.maven.apache.org/maven2/net/schmizz/sshj/0.8.1/sshj-0.8.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-sshj-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-sshj package.
Group: Data

%description data
data components for the jdk-sshj package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/sshj.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/sshj.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/sshj.xml \
%{buildroot}/usr/share/maven-poms/sshj.pom \
%{buildroot}/usr/share/java/sshj.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/sshj.jar
/usr/share/maven-metadata/sshj.xml
/usr/share/maven-poms/sshj.pom
