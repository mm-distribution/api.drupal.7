# Archive_Tar::_writeHeader()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1418–1533 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1418-L1533)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _writeHeader($p_filename, $p_stored_filename)
```

## Documentation

```text
@param string $p_filename
@param string $p_stored_filename
@return bool
```

## Code

```php
    public function _writeHeader($p_filename, $p_stored_filename)
    {
        if ($p_stored_filename == '') {
            $p_stored_filename = $p_filename;
        }

        $v_reduced_filename = $this->_pathReduction($p_stored_filename);

        if (strlen($v_reduced_filename) > 99) {
            if (!$this->_writeLongHeader($v_reduced_filename, false)) {
                return false;
            }
        }

        $v_linkname = '';
        if (@is_link($p_filename)) {
            $v_linkname = readlink($p_filename);
        }

        if (strlen($v_linkname) > 99) {
            if (!$this->_writeLongHeader($v_linkname, true)) {
                return false;
            }
        }

        $v_info = lstat($p_filename);
        $v_uid = sprintf("%07s", DecOct($v_info[4]));
        $v_gid = sprintf("%07s", DecOct($v_info[5]));
        $v_perms = sprintf("%07s", DecOct($v_info['mode'] & 000777));
        $v_mtime = sprintf("%011s", DecOct($v_info['mtime']));

        if (@is_link($p_filename)) {
            $v_typeflag = '2';
            $v_size = sprintf("%011s", DecOct(0));
        } elseif (@is_dir($p_filename)) {
            $v_typeflag = "5";
            $v_size = sprintf("%011s", DecOct(0));
        } else {
            $v_typeflag = '0';
            clearstatcache();
            $v_size = sprintf("%011s", DecOct($v_info['size']));
        }

        $v_magic = 'ustar ';
        $v_version = ' ';
        $v_uname = '';
        $v_gname = '';

        if (function_exists('posix_getpwuid')) {
            $userinfo = posix_getpwuid($v_info[4]);
            $groupinfo = posix_getgrgid($v_info[5]);

            if (isset($userinfo['name'])) {
                $v_uname = $userinfo['name'];
            }

            if (isset($groupinfo['name'])) {
                $v_gname = $groupinfo['name'];
            }
        }

        $v_devmajor = '';
        $v_devminor = '';
        $v_prefix = '';

        $v_binary_data_first = pack(
            "a100a8a8a8a12a12",
            $v_reduced_filename,
            $v_perms,
            $v_uid,
            $v_gid,
            $v_size,
            $v_mtime
        );
        $v_binary_data_last = pack(
            "a1a100a6a2a32a32a8a8a155a12",
            $v_typeflag,
            $v_linkname,
            $v_magic,
            $v_version,
            $v_uname,
            $v_gname,
            $v_devmajor,
            $v_devminor,
            $v_prefix,
            ''
        );

        // ----- Calculate the checksum
        $v_checksum = 0;
        // ..... First part of the header
        for ($i = 0; $i < 148; $i++) {
            $v_checksum += ord(substr($v_binary_data_first, $i, 1));
        }
        // ..... Ignore the checksum value and replace it by ' ' (space)
        for ($i = 148; $i < 156; $i++) {
            $v_checksum += ord(' ');
        }
        // ..... Last part of the header
        for ($i = 156, $j = 0; $i < 512; $i++, $j++) {
            $v_checksum += ord(substr($v_binary_data_last, $j, 1));
        }

        // ----- Write the first 148 bytes of the header in the archive
        $this->_writeBlock($v_binary_data_first, 148);

        // ----- Write the calculated checksum
        $v_checksum = sprintf("%06s\0 ", DecOct($v_checksum));
        $v_binary_data = pack("a8", $v_checksum);
        $this->_writeBlock($v_binary_data, 8);

        // ----- Write the last 356 bytes of the header in the archive
        $this->_writeBlock($v_binary_data_last, 356);

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
