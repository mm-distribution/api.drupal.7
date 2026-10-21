# Archive_Tar::_extractList()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 2000–2330 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L2000-L2330)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _extractList(
        $p_path,
        &$p_list_detail,
        $p_mode,
        $p_file_list,
        $p_remove_path,
        $p_preserve = false,
        $p_symlinks = true
    )
```

## Documentation

```text
@param string $p_path
@param string $p_list_detail
@param string $p_mode
@param string $p_file_list
@param string $p_remove_path
@param bool $p_preserve
@param bool $p_symlinks
@return bool
```

## Code

```php
    public function _extractList(
        $p_path,
        &$p_list_detail,
        $p_mode,
        $p_file_list,
        $p_remove_path,
        $p_preserve = false,
        $p_symlinks = true
    )
    {
        $v_result = true;
        $v_nb = 0;
        $v_extract_all = true;
        $v_listing = false;

        $p_path = $this->_translateWinPath($p_path, false);
        if ($p_path == '' || (substr($p_path, 0, 1) != '/'
                && substr($p_path, 0, 3) != "../" && !strpos($p_path, ':'))
        ) {
            $p_path = "./" . $p_path;
        }
        $p_remove_path = $this->_translateWinPath($p_remove_path);

        // ----- Look for path to remove format (should end by /)
        if (($p_remove_path != '') && (substr($p_remove_path, -1) != '/')) {
            $p_remove_path .= '/';
        }
        $p_remove_path_size = strlen($p_remove_path);

        switch ($p_mode) {
            case "complete" :
                $v_extract_all = true;
                $v_listing = false;
                break;
            case "partial" :
                $v_extract_all = false;
                $v_listing = false;
                break;
            case "list" :
                $v_extract_all = false;
                $v_listing = true;
                break;
            default :
                $this->_error('Invalid extract mode (' . $p_mode . ')');
                return false;
        }

        clearstatcache();

        while (strlen($v_binary_data = $this->_readBlock()) != 0) {
            $v_extract_file = false;
            $v_extraction_stopped = 0;

            if (!$this->_readHeader($v_binary_data, $v_header)) {
                return false;
            }

            if ($v_header['filename'] == '') {
                continue;
            }

            switch ($v_header['typeflag']) {
                case 'L':
                    {
                        if (!$this->_readLongHeader($v_header)) {
                            return null;
                        }
                    }
                    break;

                case 'K':
                    {
                        $v_link_header = $v_header;
                        if (!$this->_readLongHeader($v_link_header)) {
                            return null;
                        }
                        $v_header['link'] = $v_link_header['filename'];
                    }
                    break;
            }

            // ignore extended / pax headers
            if ($v_header['typeflag'] == 'x' || $v_header['typeflag'] == 'g') {
                $this->_jumpBlock(ceil(($v_header['size'] / 512)));
                continue;
            }

            if ((!$v_extract_all) && (is_array($p_file_list))) {
                // ----- By default no unzip if the file is not found
                $v_extract_file = false;

                for ($i = 0; $i < sizeof($p_file_list); $i++) {
                    // ----- Look if it is a directory
                    if (substr($p_file_list[$i], -1) == '/') {
                        // ----- Look if the directory is in the filename path
                        if ((strlen($v_header['filename']) > strlen($p_file_list[$i]))
                            && (substr($v_header['filename'], 0, strlen($p_file_list[$i]))
                                == $p_file_list[$i])
                        ) {
                            $v_extract_file = true;
                            break;
                        }
                    } // ----- It is a file, so compare the file names
                    elseif ($p_file_list[$i] == $v_header['filename']) {
                        $v_extract_file = true;
                        break;
                    }
                }
            } else {
                $v_extract_file = true;
            }

            // ----- Look if this file need to be extracted
            if (($v_extract_file) && (!$v_listing)) {
                if (($p_remove_path != '')
                    && (substr($v_header['filename'] . '/', 0, $p_remove_path_size)
                        == $p_remove_path)
                ) {
                    $v_header['filename'] = substr(
                        $v_header['filename'],
                        $p_remove_path_size
                    );
                    if ($v_header['filename'] == '') {
                        continue;
                    }
                }
                if (($p_path != './') && ($p_path != '/')) {
                    while (substr($p_path, -1) == '/') {
                        $p_path = substr($p_path, 0, strlen($p_path) - 1);
                    }

                    if (substr($v_header['filename'], 0, 1) == '/') {
                        $v_header['filename'] = $p_path . $v_header['filename'];
                    } else {
                        $v_header['filename'] = $p_path . '/' . $v_header['filename'];
                    }
                }
                if (file_exists($v_header['filename'])) {
                    if ((@is_dir($v_header['filename']))
                        && ($v_header['typeflag'] == '')
                    ) {
                        $this->_error(
                            'File ' . $v_header['filename']
                            . ' already exists as a directory'
                        );
                        return false;
                    }
                    if (($this->_isArchive($v_header['filename']))
                        && ($v_header['typeflag'] == "5")
                    ) {
                        $this->_error(
                            'Directory ' . $v_header['filename']
                            . ' already exists as a file'
                        );
                        return false;
                    }
                    if (!is_writeable($v_header['filename'])) {
                        $this->_error(
                            'File ' . $v_header['filename']
                            . ' already exists and is write protected'
                        );
                        return false;
                    }
                    if (filemtime($v_header['filename']) > $v_header['mtime']) {
                        // To be completed : An error or silent no replace ?
                    }
                } // ----- Check the directory availability and create it if necessary
                elseif (($v_result
                        = $this->_dirCheck(
                        ($v_header['typeflag'] == "5"
                            ? $v_header['filename']
                            : dirname($v_header['filename']))
                    )) != 1
                ) {
                    $this->_error('Unable to create path for ' . $v_header['filename']);
                    return false;
                }

                if ($v_extract_file) {
                    if ($v_header['typeflag'] == "5") {
                        if (!@file_exists($v_header['filename'])) {
                            if (!@mkdir($v_header['filename'], 0775)) {
                                $this->_error(
                                    'Unable to create directory {'
                                    . $v_header['filename'] . '}'
                                );
                                return false;
                            }
                        }
                    } elseif ($v_header['typeflag'] == "2") {
                        if (!$p_symlinks) {
                            $this->_warning('Symbolic links are not allowed. '
                                . 'Unable to extract {'
                                . $v_header['filename'] . '}'
                            );
                            return false;
                        }
                        $absolute_link = FALSE;
                        $link_depth = 0;
                        if (strpos($v_header['link'], "/") === 0 || strpos($v_header['link'], ':') !== FALSE) {
                          $absolute_link = TRUE;
                        }
                        else {
                            $s_filename = preg_replace('@^' . preg_quote($p_path) . '@', "", $v_header['filename']);
                            $s_linkname = str_replace('\\', '/', $v_header['link']);
                            foreach (explode("/", $s_filename) as $dir) {
                                if ($dir === "..") {
                                    $link_depth--;
                                } elseif ($dir !== "" && $dir !== "." ) {
                                    $link_depth++;
                                }
                            }
                            foreach (explode("/", $s_linkname) as $dir){
                                if ($link_depth <= 0) {
                                    break;
                                }
                                if ($dir === "..") {
                                    $link_depth--;
                                } elseif ($dir !== "" && $dir !== ".") {
                                    $link_depth++;
                                }
                            }
                        }
                        if ($absolute_link || $link_depth <= 0) {
                            $this->_error(
                                 'Out-of-path file extraction {'
                                 . $v_header['filename'] . ' --> ' .
                                 $v_header['link'] . '}'
                            );
                            return false;
                        }
                        if (@file_exists($v_header['filename'])) {
                            @drupal_unlink($v_header['filename']);
                        }
                        if (!@symlink($v_header['link'], $v_header['filename'])) {
                            $this->_error(
                                'Unable to extract symbolic link {'
                                . $v_header['filename'] . '}'
                            );
                            return false;
                        }
                    } else {
                        if (($v_dest_file = @fopen($v_header['filename'], "wb")) == 0) {
                            $this->_error(
                                'Error while opening {' . $v_header['filename']
                                . '} in write binary mode'
                            );
                            return false;
                        } else {
                            $n = floor($v_header['size'] / 512);
                            for ($i = 0; $i < $n; $i++) {
                                $v_content = $this->_readBlock();
                                fwrite($v_dest_file, $v_content, 512);
                            }
                            if (($v_header['size'] % 512) != 0) {
                                $v_content = $this->_readBlock();
                                fwrite($v_dest_file, $v_content, ($v_header['size'] % 512));
                            }

                            @fclose($v_dest_file);

                            if ($p_preserve) {
                                @chown($v_header['filename'], $v_header['uid']);
                                @chgrp($v_header['filename'], $v_header['gid']);
                            }

                            // ----- Change the file mode, mtime
                            @touch($v_header['filename'], $v_header['mtime']);
                            if ($v_header['mode'] & 0111) {
                                // make file executable, obey umask
                                $mode = fileperms($v_header['filename']) | (~umask() & 0111);
                                @chmod($v_header['filename'], $mode);
                            }
                        }

                        // ----- Check the file size
                        clearstatcache();
                        if (!is_file($v_header['filename'])) {
                            $this->_error(
                                'Extracted file ' . $v_header['filename']
                                . 'does not exist. Archive may be corrupted.'
                            );
                            return false;
                        }

                        $filesize = filesize($v_header['filename']);
                        if ($filesize != $v_header['size']) {
                            $this->_error(
                                'Extracted file ' . $v_header['filename']
                                . ' does not have the correct file size \''
                                . $filesize
                                . '\' (' . $v_header['size']
                                . ' expected). Archive may be corrupted.'
                            );
                            return false;
                        }
                    }
                } else {
                    $this->_jumpBlock(ceil(($v_header['size'] / 512)));
                }
            } else {
                $this->_jumpBlock(ceil(($v_header['size'] / 512)));
            }

            /* TBC : Seems to be unused ...
            if ($this->_compress)
              $v_end_of_file = @gzeof($this->_file);
            else
              $v_end_of_file = @feof($this->_file);
              */

            if ($v_listing || $v_extract_file || $v_extraction_stopped) {
                // ----- Log extracted files
                if (($v_file_dir = dirname($v_header['filename']))
                    == $v_header['filename']
                ) {
                    $v_file_dir = '';
                }
                if ((substr($v_header['filename'], 0, 1) == '/') && ($v_file_dir == '')) {
                    $v_file_dir = '/';
                }

                $p_list_detail[$v_nb++] = $v_header;
                if (is_array($p_file_list) && (count($p_list_detail) == count($p_file_list))) {
                    return true;
                }
            }
        }

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
