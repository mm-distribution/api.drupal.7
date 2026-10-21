# Archive_Tar::_writeHeaderBlock()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1545–1653 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1545-L1653)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _writeHeaderBlock(
        $p_filename,
        $p_size,
        $p_mtime = 0,
        $p_perms = 0,
        $p_type = '',
        $p_uid = 0,
        $p_gid = 0
    )
```

## Documentation

```text
@param string $p_filename
@param int $p_size
@param int $p_mtime
@param int $p_perms
@param string $p_type
@param int $p_uid
@param int $p_gid
@return bool
```

## Code

```php
    public function _writeHeaderBlock(
        $p_filename,
        $p_size,
        $p_mtime = 0,
        $p_perms = 0,
        $p_type = '',
        $p_uid = 0,
        $p_gid = 0
    )
    {
        $p_filename = $this->_pathReduction($p_filename);

        if (strlen($p_filename) > 99) {
            if (!$this->_writeLongHeader($p_filename, false)) {
                return false;
            }
        }

        if ($p_type == "5") {
            $v_size = sprintf("%011s", DecOct(0));
        } else {
            $v_size = sprintf("%011s", DecOct($p_size));
        }

        $v_uid = sprintf("%07s", DecOct($p_uid));
        $v_gid = sprintf("%07s", DecOct($p_gid));
        $v_perms = sprintf("%07s", DecOct($p_perms & 000777));

        $v_mtime = sprintf("%11s", DecOct($p_mtime));

        $v_linkname = '';

        $v_magic = 'ustar ';

        $v_version = ' ';

        if (function_exists('posix_getpwuid')) {
            $userinfo = posix_getpwuid($p_uid);
            $groupinfo = posix_getgrgid($p_gid);

            if ($userinfo === false || $groupinfo === false) {
                $v_uname = '';
                $v_gname = '';
            } else {
                $v_uname = $userinfo['name'];
                $v_gname = $groupinfo['name'];
            }
        } else {
            $v_uname = '';
            $v_gname = '';
        }

        $v_devmajor = '';

        $v_devminor = '';

        $v_prefix = '';

        $v_binary_data_first = pack(
            "a100a8a8a8a12A12",
            $p_filename,
            $v_perms,
            $v_uid,
            $v_gid,
            $v_size,
            $v_mtime
        );
        $v_binary_data_last = pack(
            "a1a100a6a2a32a32a8a8a155a12",
            $p_type,
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
        $v_checksum = sprintf("%06s ", DecOct($v_checksum));
        $v_binary_data = pack("a8", $v_checksum);
        $this->_writeBlock($v_binary_data, 8);

        // ----- Write the last 356 bytes of the header in the archive
        $this->_writeBlock($v_binary_data_last, 356);

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
