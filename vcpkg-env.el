(require 'cl-lib)
(require 'yekneb-constants)
(require 'yekneb-debug)
(require 'yekneb-env)
(require 'yekneb-path-manip)
(require 'yekneb-string-utilities)


(defconst vcpkg--add-to-path-x64-linux
  '(
    "${VCPKG_ROOT}/downloads/tools/cmake-3.31.10-linux/cmake-3.31.10-linux-x86_64/bin"
    "${VCPKG_ROOT}/downloads/tools/meson-1.9.0-d1fcc2"
    "${VCPKG_ROOT}/downloads/tools/ninja-1.13.2-linux"
    "${VCPKG_ROOT}/downloads/tools/patchelf/0.15.5-x86_64-linux/bin"
    "${VCPKG_ROOT}/installed/x64-linux/tools"
    )
  "Directories to add to the path for x64-linux."
  )

(defconst vcpkg--add-to-path-x64-mingw-dynamic
  '(
    "${VCPKG_ROOT}/downloads/tools/7zip-25.01-windows"
    "${VCPKG_ROOT}/downloads/tools/7zr-25.01-windows"
    "${VCPKG_ROOT}/downloads/tools/meson-1.9.0-d1fcc2"
    "${VCPKG_ROOT}/downloads/tools/ninja-1.13.2-windows"
    "${VCPKG_ROOT}/downloads/tools/python/python-3.14.2-x64-1"
    "${VCPKG_ROOT}/installed/x64-mingw-dynamic/tools"
    )
  "Directories to add to the path for x64-mingw-dynamic."
  )

(defconst vcpkg--add-to-path-x64-windows
  '(
    "${VCPKG_ROOT}/downloads/tools/cmake-3.30.1-windows/cmake-3.30.1-windows-i386/bin"
    "${VCPKG_ROOT}/downloads/tools/jom/jom-1_1_4"
    "${VCPKG_ROOT}/downloads/tools/nasm/nasm-2.16.03"
    "${VCPKG_ROOT}/downloads/tools/perl/5.42.0.1/c/bin"
    "${VCPKG_ROOT}/downloads/tools/perl/5.42.0.1/c/x86_64-w64-mingw32/bin"
    "${VCPKG_ROOT}/downloads/tools/perl/5.42.0.1/perl/site/bin"
    "${VCPKG_ROOT}/downloads/tools/perl/5.42.0.1/perl/bin"
    "${VCPKG_ROOT}/downloads/tools/python/python-3.12.7-x64"
    "${VCPKG_ROOT}/downloads/tools/python/python-3.12.7-x64-1"
    "${VCPKG_ROOT}/downloads/tools/win_bison/2.5.24"
    "${VCPKG_ROOT}/installed/x64-windows/bin"
    "${VCPKG_ROOT}/installed/x64-windows/tools"
   )
  "Directories to add to the path for x64-windows."
 )

(cl-defun add-tools-directories-to-path (tools-dir)
  (yekneb-log yekneb-log-info "tools-dir is '%s'." tools-dir)
  (yekneb-log yekneb-log-info "Adding the directories in tool-dirs to the path.")
  (when (file-directory-p tools-dir)
    (setq tool-dirs (directory-files tools-dir))
    (dolist (tool-dir tool-dirs)
      (when (and (not (string= tool-dir ".")) (not (string= tool-dir "..")))
        (setq tool-dir (expand-file-name tool-dir tools-dir))
        (when (file-directory-p tool-dir)
          (yekneb-add-to-path tool-dir t)
          )
        (setq tool-dir (expand-file-name "bin" tool-dir))
        (when (file-directory-p tool-dir)
          (yekneb-add-to-path tool-dir t)
          )
        )
      )
      (cl-return-from add-tools-directories-to-path t)
    )
  (cl-return-from add-tools-directories-to-path nil)
  )

(defun update-environment-for-vcpkg-x64-linux ()
  "Updates the environment for VCPKG for x64-linux."
  (let
    (
     (yekneb-debug-level (if init-file-debug yekneb-log-debug yekneb-log-entry))
     (load-file-dir (file-name-directory load-file-name))
     (tool-dirs nil)
     (tools-dir "${VCPKG_ROOT}/installed/x64-linux/tools")
     )
    (setq tools-dir (substitute-env-vars tools-dir))
    (yekneb-log yekneb-log-info "Adding the directories in vcpkg--add-to-path-x64-linux to the path.")
    (yekneb-add-dirs-to-path vcpkg--add-to-path-x64-linux t t load-file-dir)
    (yekneb-log yekneb-log-info "Adding the directories in tool-dirs to the path.")
    (add-tools-directories-to-path tools-dir)
    )
  )

(defun update-environment-for-vcpkg-x64-mingw-dynamic ()
  "Updates the environment for VCPKG for x64-mingw-dynamic."
  (let
    (
     (yekneb-debug-level (if init-file-debug yekneb-log-debug yekneb-log-entry))
     (load-file-dir (file-name-directory load-file-name))
     (tool-dirs nil)
     (tools-dir "${VCPKG_ROOT}/installed/x64-mingw-dynamic/tools")
     (poedit-dirs
      '(
        "${ProgramFiles(x86)}/Poedit"
        "${ProgramFiles(x86)}/Poedit/GettextTools/bin"
        )
      )
     )
    (setq tools-dir (substitute-env-vars tools-dir))
    (yekneb-log yekneb-log-info "Adding the directories in vcpkg--add-to-path-x64-mingw-dynamic to the path.")
    (yekneb-add-dirs-to-path vcpkg--add-to-path-x64-mingw-dynamic t t load-file-dir)
    (add-tools-directories-to-path tools-dir)
    (yekneb-log yekneb-log-info "Adding the directories in poedit-dirs to the path.")
    (yekneb-add-dirs-to-path poedit-dirs t t load-file-dir)
    )
  )

(defun update-environment-for-vcpkg-x64-windows ()
  "Updates the environment for VCPKG for x64-windows."
  (let
    (
     (yekneb-debug-level (if init-file-debug yekneb-log-debug yekneb-log-entry))
     (load-file-dir (file-name-directory load-file-name))
     (tool-dirs nil)
     (tools-dir "${VCPKG_ROOT}/installed/x64-windows/tools")
     (poedit-dirs
      '(
        "${ProgramFiles(x86)}/Poedit"
        "${ProgramFiles(x86)}/Poedit/GettextTools/bin"
        )
      )
     )
    (setq tools-dir (substitute-env-vars tools-dir))
    (yekneb-log yekneb-log-info "Adding the directories in vcpkg--add-to-path-x64-windows to the path.")
    (yekneb-add-dirs-to-path vcpkg--add-to-path-x64-windows t t load-file-dir)
    (add-tools-directories-to-path tools-dir)
    (yekneb-log yekneb-log-info "Adding the directories in poedit-dirs to the path.")
    (yekneb-add-dirs-to-path poedit-dirs t t load-file-dir)
    )
  )

(cl-defun update-environment-for-vcpkg ()
  "Updates the environment for VCPKG."
  (let ((VCPKG_ROOT (getenv "VCPKG_ROOT")))
    (when (yekneb-empty-string-p VCPKG_ROOT)
      (cl-return-from update-environment-for-vcpkg nil)
      )
    )
  (when (eq system-type 'windows-nt)
    (when (file-directory-p (substitute-env-vars "${VCPKG_ROOT}/installed/x64-mingw-dynamic"))
      (update-environment-for-vcpkg-x64-mingw-dynamic)
      (cl-return-from update-environment-for-vcpkg t)
      )
    (when (file-directory-p (substitute-env-vars "${VCPKG_ROOT}/installed/x64-windows"))
      (update-environment-for-vcpkg-x64-windows)
      (cl-return-from update-environment-for-vcpkg t)
      )
    )
  (when (eq system-type 'gnu/linux)
    (update-environment-for-vcpkg-x64-linux)
    (cl-return-from update-environment-for-vcpkg t)
    )
  (cl-return-from update-environment-for-vcpkg nil)
  )

(update-environment-for-vcpkg)
