# Challenge

<p align="center">
  <img src="./Image/stPart1-1.png" alt="Entry point"/>
</p>

# File: [story](./story)

# Solve:

```bash
nguyenguyen753@MochiZou:~/CTF/bcaCtf/RE/story$ file story 
story: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=ccea544c84172f60a939819e4416fdd108982090, for GNU/Linux 3.2.0, not stripped
```
```bash
nguyenguyen753@MochiZou:~/CTF/bcaCtf/RE/story$ strings story 
/lib64/ld-linux-x86-64.so.2
libc.so.6
nanosleep
puts
__stack_chk_fail
__cxa_finalize
__libc_start_main
GLIBC_2.4
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
dH34%(
[]A\A]A^A_
bcactf{w0ol_m4k3s_str1ng_ziv4mk3ca91b}
Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full.
One for the master,
One for the dame,
And one for the little boy
Who lives down the lane
Did you know? I almost used "Little Miss Muffet" for this problem.
Spiders make string too, kind of.
:*3$"
GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8060
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
main.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
_ITM_deregisterTMCloneTable
puts@@GLIBC_2.2.5
_edata
sleepNanos
__stack_chk_fail@@GLIBC_2.4
nanosleep@@GLIBC_2.2.5
__libc_start_main@@GLIBC_2.2.5
__data_start
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_csu_init
__bss_start
main
__TMC_END__
_ITM_registerTMCloneTable
__cxa_finalize@@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.plt.sec
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
```

`bcactf{w0ol_m4k3s_str1ng_ziv4mk3ca91b}`