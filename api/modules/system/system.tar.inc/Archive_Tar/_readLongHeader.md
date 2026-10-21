# Archive_Tar::_readLongHeader()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1885–1917 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1885-L1917)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _readLongHeader(&$v_header)
```

## Documentation

```text
@param $v_header
@return bool
```

## Code

```php
    public function _readLongHeader(&$v_header)
    {
        $v_filename = '';
        $v_filesize = $v_header['size'];
        $n = floor($v_header['size'] / 512);
        for ($i = 0; $i < $n; $i++) {
            $v_content = $this->_readBlock();
            $v_filename .= $v_content;
        }
        if (($v_header['size'] % 512) != 0) {
            $v_content = $this->_readBlock();
            $v_filename .= $v_content;
        }

        // ----- Read the next header
        $v_binary_data = $this->_readBlock();

        if (!$this->_readHeader($v_binary_data, $v_header)) {
            return false;
        }

        $v_filename = rtrim(substr($v_filename, 0, $v_filesize), "\0");
        $v_header['filename'] = $v_filename;
        if ($this->_isMaliciousFilename($v_filename)) {
            $this->_error(
                'Malicious .tar detected, file "' . $v_filename .
                '" will not install in desired directory tree'
            );
            return false;
        }

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
