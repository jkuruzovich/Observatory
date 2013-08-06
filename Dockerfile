FROM ubuntu:12.04
MAINTAINER Colin Rice
ADD docker/sources.list /etc/apt/sources.list
ADD http://apt.puppetlabs.com/puppetlabs-release-precise.deb /puppetlabs-release-precise.deb 
RUN dpkg -i /puppetlabs-release-precise.deb
RUN rm /puppetlabs-release-precise.deb
RUN apt-get update -qy
RUN apt-get install puppet -yq
ADD . /vagrant
RUN puppet apply --modulepath "/vagrant/modules" /vagrant/puppet/base.pp --detailed-exitcodes || [ $? -eq 2 ]
RUN rm -r /vagrant

EXPOSE 80
