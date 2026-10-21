# Archive_Tar::_extractInString()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1927–1988 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1927-L1988)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
private function _extractInString($p_filename)
```

## Documentation

```text
This method extract from the archive one file identified by $p_filename.
The return value is a string with the file content, or null on error.

@param string $p_filename The path of the file to extract in a string.

@return a string with the file content or null.
```

## Code

```php
    private function _extractInString($p_filename)
    {
        $v_result_str = "";

        while (strlen($v_binary_data = $this->_readBlock()) != 0) {
            if (!$this->_readHeader($v_binary_data, $v_header)) {
                return null;
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

            if ($v_header['filename'] == $p_filename) {
                if ($v_header['typeflag'] == "5") {
                    $this->_error(
                        'Unable to extract in string a directory '
                        . 'entry {' . $v_header['filename'] . '}'
                    );
                    return null;
                } else {
                    $n = floor($v_header['size'] / 512);
                    for ($i = 0; $i < $n; $i++) {
                        $v_result_str .= $this->_readBlock();
                    }
                    if (($v_header['size'] % 512) != 0) {
                        $v_content = $this->_readBlock();
                        $v_result_str .= substr(
                            $v_content,
                            0,
                            ($v_header['size'] % 512)
                        );
                    }
                    return $v_result_str;
                }
            } else {
                $this->_jumpBlock(ceil(($v_header['size'] / 512)));
            }
        }

        return null;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
