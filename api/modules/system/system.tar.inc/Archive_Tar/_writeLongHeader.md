# Archive_Tar::_writeLongHeader()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1659–1733 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1659-L1733)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _writeLongHeader($p_filename, $is_link = false)
```

## Documentation

```text
@param string $p_filename
@return bool
```

## Code

```php
    public function _writeLongHeader($p_filename, $is_link = false)
    {
        $v_uid = sprintf("%07s", 0);
        $v_gid = sprintf("%07s", 0);
        $v_perms = sprintf("%07s", 0);
        $v_size = sprintf("%'011s", DecOct(strlen($p_filename)));
        $v_mtime = sprintf("%011s", 0);
        $v_typeflag = ($is_link ? 'K' : 'L');
        $v_linkname = '';
        $v_magic = 'ustar ';
        $v_version = ' ';
        $v_uname = '';
        $v_gname = '';
        $v_devmajor = '';
        $v_devminor = '';
        $v_prefix = '';

        $v_binary_data_first = pack(
            "a100a8a8a8a12a12",
            '././@LongLink',
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

        // ----- Write the filename as content of the block
        $i = 0;
        while (($v_buffer = substr($p_filename, (($i++) * 512), 512)) != '') {
            $v_binary_data = pack("a512", "$v_buffer");
            $this->_writeBlock($v_binary_data);
        }

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
