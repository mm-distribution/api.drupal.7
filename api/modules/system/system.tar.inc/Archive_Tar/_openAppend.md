# Archive_Tar::_openAppend()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 2335–2467 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L2335-L2467)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _openAppend()
```

## Documentation

```text
@return bool
```

## Code

```php
    public function _openAppend()
    {
        if (filesize($this->_tarname) == 0) {
            return $this->_openWrite();
        }

        if ($this->_compress) {
            $this->_close();

            if (!@rename($this->_tarname, $this->_tarname . ".tmp")) {
                $this->_error(
                    'Error while renaming \'' . $this->_tarname
                    . '\' to temporary file \'' . $this->_tarname
                    . '.tmp\''
                );
                return false;
            }

            if ($this->_compress_type == 'gz') {
                $v_temp_tar = @gzopen($this->_tarname . ".tmp", "rb");
            } elseif ($this->_compress_type == 'bz2') {
                $v_temp_tar = @bzopen($this->_tarname . ".tmp", "r");
            } elseif ($this->_compress_type == 'lzma2') {
                $v_temp_tar = @xzopen($this->_tarname . ".tmp", "r");
            }


            if ($v_temp_tar == 0) {
                $this->_error(
                    'Unable to open file \'' . $this->_tarname
                    . '.tmp\' in binary read mode'
                );
                @rename($this->_tarname . ".tmp", $this->_tarname);
                return false;
            }

            if (!$this->_openWrite()) {
                @rename($this->_tarname . ".tmp", $this->_tarname);
                return false;
            }

            if ($this->_compress_type == 'gz') {
                $end_blocks = 0;

                while (!@gzeof($v_temp_tar)) {
                    $v_buffer = @gzread($v_temp_tar, 512);
                    if ($v_buffer == ARCHIVE_TAR_END_BLOCK || strlen($v_buffer) == 0) {
                        $end_blocks++;
                        // do not copy end blocks, we will re-make them
                        // after appending
                        continue;
                    } elseif ($end_blocks > 0) {
                        for ($i = 0; $i < $end_blocks; $i++) {
                            $this->_writeBlock(ARCHIVE_TAR_END_BLOCK);
                        }
                        $end_blocks = 0;
                    }
                    $v_binary_data = pack("a512", $v_buffer);
                    $this->_writeBlock($v_binary_data);
                }

                @gzclose($v_temp_tar);
            } elseif ($this->_compress_type == 'bz2') {
                $end_blocks = 0;

                while (strlen($v_buffer = @bzread($v_temp_tar, 512)) > 0) {
                    if ($v_buffer == ARCHIVE_TAR_END_BLOCK || strlen($v_buffer) == 0) {
                        $end_blocks++;
                        // do not copy end blocks, we will re-make them
                        // after appending
                        continue;
                    } elseif ($end_blocks > 0) {
                        for ($i = 0; $i < $end_blocks; $i++) {
                            $this->_writeBlock(ARCHIVE_TAR_END_BLOCK);
                        }
                        $end_blocks = 0;
                    }
                    $v_binary_data = pack("a512", $v_buffer);
                    $this->_writeBlock($v_binary_data);
                }

                @bzclose($v_temp_tar);
            } elseif ($this->_compress_type == 'lzma2') {
                $end_blocks = 0;

                while (strlen($v_buffer = @xzread($v_temp_tar, 512)) > 0) {
                    if ($v_buffer == ARCHIVE_TAR_END_BLOCK || strlen($v_buffer) == 0) {
                        $end_blocks++;
                        // do not copy end blocks, we will re-make them
                        // after appending
                        continue;
                    } elseif ($end_blocks > 0) {
                        for ($i = 0; $i < $end_blocks; $i++) {
                            $this->_writeBlock(ARCHIVE_TAR_END_BLOCK);
                        }
                        $end_blocks = 0;
                    }
                    $v_binary_data = pack("a512", $v_buffer);
                    $this->_writeBlock($v_binary_data);
                }

                @xzclose($v_temp_tar);
            }

            if (!@drupal_unlink($this->_tarname . ".tmp")) {
                $this->_error(
                    'Error while deleting temporary file \''
                    . $this->_tarname . '.tmp\''
                );
            }
        } else {
            // ----- For not compressed tar, just add files before the last
            //       one or two 512 bytes block
            if (!$this->_openReadWrite()) {
                return false;
            }

            clearstatcache();
            $v_size = filesize($this->_tarname);

            // We might have zero, one or two end blocks.
            // The standard is two, but we should try to handle
            // other cases.
            fseek($this->_file, $v_size - 1024);
            if (fread($this->_file, 512) == ARCHIVE_TAR_END_BLOCK) {
                fseek($this->_file, $v_size - 1024);
            } elseif (fread($this->_file, 512) == ARCHIVE_TAR_END_BLOCK) {
                fseek($this->_file, $v_size - 512);
            }
        }

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
