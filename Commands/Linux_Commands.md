
#########################################################

# Linux Commands && Options :

### Classics :

sudo apt-get autoremove
sudo apt-get clean
sudo apt-get autoclean
sudo apt-get update
sudo apt-get upgrade
sudo apt-get upgrade --fix-missing

### How to get help :

	-h or –help (ex : wget –help | less)

	wget –help | grep proxy (to target what you're looking for)

	help (commmand)

	man (manual, ex : man wget)

	info (ex: info tar)



		### A

			alias (see http://www.linfo.org/alias.html), a way to run a command or a series of Unix commands using a shorter name than those that are usually associated with such commands.

		### B

		### C

			cat
			cd
			chmod  - u(ser) -g(roup) -o(thers)

			chown, changes file or group ownership and has the option to change ownership of all objects within a directory tree, as well as having the ability to view information on objects processed.
			
			cmp, the cmp utility compares two files of any type and writes the results to the standard output. By default, cmp is silent if the files are the same; if they differ, the byte and line number at which the first difference occurred is reported.
			
			cp

		### D

			date,  sets a system's date and time. This is also a useful way to output/print current information when working in a script file.
			df, displays the amount of disk space available on the file system containing each file name argument. With no file name, available space on all currently mounted file systems is shown.
			diff -q (reports if 2 files differ or not only)

		### E

			exit
			export, converts a file into a different format than the one in which it is currently. Once a file is exported, it can be accessed by any application that uses its format.

		### F

			find, searches the directory tree to find particular groups of files that meet specified conditions, including --name and --type, -exec and --size and --mtime and --user.

		### G

			grep -ri(recursive & ignore cases) -l (only file name no text lines) -n(umbers of the lines it found a hit) -l(only liste files where nothing has been found)

		### H

		### I

		### J

		### K

		### L

			less, more
			ln -s (create symbolic link)
			The ln command creates a new name for a file through hard linking, allowing multiple users to share one file.

		### M

		### N

		### O

		### P

			ps, reports the statuses of current processes in a system.
			pwd

		### Q

		### R

			RPM, Red Hat Package Manager (RPM) is a command-line-driven program capable of installing, uninstalling and managing software packages in Linux.

		### S

			sdiff, finds differences between two files by producing a side-by-side listing indicating lines that are dissimilar. Sdiff then merges the files and outputs results to the outfile.
			shutdown
			Snort, snort is an open source network intrusion detection system and packet sniffer that monitors network traffic, looking at each packet to detect dangerous payloads or suspicious anomalies. Snort is based on libpcap.
			sort, used to sort lines of text alphabetically or numerically according to fields; multiple sort keys can also be used.
			sudo, allows a system admin to give certain users the ability to run some (or all) commands at the root level and logs all commands and arguments.
			ssh, SSH is a command interface used for securely gaining access to a remote computer and is used by network admins to control servers remotely.


		### T

			tar

		### U

		### V

			vi, is a text editor that allows a user to control the system by solely using the keyboard instead of a combination of mouse selections and keystrokes.
			vmstat, is used to get a snapshot of everything in a system and to report information on such items as processes, memory, paging and CPU activity. This is a good method for admins to use to determine where issues/slowdown in a system may be occurring.

		### W

			wc, counts the number of words, lines and characters in text files and produces a count for multiple files if several files are selected.
			wget, is a network utility that retrieves files from the web that support http, https and ftp protocols. Wget works non-interactively in the background while a user is logged off. This can create local versions of remote websites, re-creating directories of original sites.
			whoami, prints or writes the user/login name associated with the current user ID to the standard output.

		### X

		### Y

		### Z


# Fun commands :

watch -n1 --difference "echo "Uptime"; uptime; echo \n ; ps -eo pcpu,pid,args | sort -k 1 -r |grep -v watch | head -10; echo "\n" ; tail /var/log/cron| grep check_load"

history|awk '{print $2}' |awk '{print $1}' | sort | uniq -c | sort -rn | head -10


