# Archive_Tar::_readHeader()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1740–1827 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1740-L1827)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _readHeader($v_binary_data, &$v_header)
```

## Documentation

```text
@param mixed $v_binary_data
@param mixed $v_header
@return bool
```

## Code

```php
    public function _readHeader($v_binary_data, &$v_header)
    {
        if (strlen($v_binary_data) == 0) {
            $v_header['filename'] = '';
            return true;
        }

        if (strlen($v_binary_data) != 512) {
            $v_header['filename'] = '';
            $this->_error('Invalid block size : ' . strlen($v_binary_data));
            return false;
        }

        if (!is_array($v_header)) {
            $v_header = array();
        }
        // ----- Calculate the checksum
        $v_checksum = 0;
        // ..... First part of the header
        $v_binary_split = str_split($v_binary_data);
        $v_checksum += array_sum(array_map('ord', array_slice($v_binary_split, 0, 148)));
        $v_checksum += array_sum(array_map('ord', array(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',)));
        $v_checksum += array_sum(array_map('ord', array_slice($v_binary_split, 156, 512)));


        $v_data = unpack($this->_fmt, $v_binary_data);

        if (strlen($v_data["prefix"]) > 0) {
            $v_data["filename"] = "$v_data[prefix]/$v_data[filename]";
        }

        // ----- Extract the checksum
        $v_data_checksum = trim($v_data['checksum']);
        if (!preg_match('/^[0-7]*$/', $v_data_checksum)) {
            $this->_error(
                'Invalid checksum for file "' . $v_data['filename']
                . '" : ' . $v_data_checksum . ' extracted'
            );
            return false;
        }

        $v_header['checksum'] = OctDec($v_data_checksum);
        if ($v_header['checksum'] != $v_checksum) {
            $v_header['filename'] = '';

            // ----- Look for last block (empty block)
            if (($v_checksum == 256) && ($v_header['checksum'] == 0)) {
                return true;
            }

            $this->_error(
                'Invalid checksum for file "' . $v_data['filename']
                . '" : ' . $v_checksum . ' calculated, '
                . $v_header['checksum'] . ' expected'
            );
            return false;
        }

        // ----- Extract the properties
        $v_header['filename'] = rtrim($v_data['filename'], "\0");
        if ($this->_isMaliciousFilename($v_header['filename'])) {
            $this->_error(
                'Malicious .tar detected, file "' . $v_header['filename'] .
                '" will not install in desired directory tree'
            );
            return false;
        }
        $v_header['mode'] = OctDec(trim($v_data['mode']));
        $v_header['uid'] = OctDec(trim($v_data['uid']));
        $v_header['gid'] = OctDec(trim($v_data['gid']));
        $v_header['size'] = $this->_tarRecToSize($v_data['size']);
        $v_header['mtime'] = OctDec(trim($v_data['mtime']));
        if (($v_header['typeflag'] = $v_data['typeflag']) == "5") {
            $v_header['size'] = 0;
        }
        $v_header['link'] = trim($v_data['link']);
        /* ----- All these fields are removed form the header because
        they do not carry interesting info
        $v_header[magic] = trim($v_data[magic]);
        $v_header[version] = trim($v_data[version]);
        $v_header[uname] = trim($v_data[uname]);
        $v_header[gname] = trim($v_data[gname]);
        $v_header[devmajor] = trim($v_data[devmajor]);
        $v_header[devminor] = trim($v_data[devminor]);
        */

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
