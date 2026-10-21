# Archive_Tar::__construct()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 172–277 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L172-L277)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function __construct($p_tarname, $p_compress = null, $buffer_length = 512)
```

## Documentation

```text
Archive_Tar Class constructor. This flavour of the constructor only
declare a new Archive_Tar object, identifying it by the name of the
tar file.
If the compress argument is set the tar will be read or created as a
gzip or bz2 compressed TAR file.

@param string $p_tarname The name of the tar archive to create
@param string $p_compress can be null, 'gz', 'bz2' or 'lzma2'. This
              parameter indicates if gzip, bz2 or lzma2 compression
              is required.  For compatibility reason the
              boolean value 'true' means 'gz'.
@param int $buffer_length Length of the read buffer in bytes

@return bool
```

## Code

```php
    public function __construct($p_tarname, $p_compress = null, $buffer_length = 512)
    {
        // Drupal removal parent::__construct().

        $this->_compress = false;
        $this->_compress_type = 'none';
        if (($p_compress === null) || ($p_compress == '')) {
            if (@file_exists($p_tarname)) {
                if ($fp = @fopen($p_tarname, "rb")) {
                    // look for gzip magic cookie
                    $data = fread($fp, 2);
                    fclose($fp);
                    if ($data == "\37\213") {
                        $this->_compress = true;
                        $this->_compress_type = 'gz';
                        // No sure it's enought for a magic code ....
                    } elseif ($data == "BZ") {
                        $this->_compress = true;
                        $this->_compress_type = 'bz2';
                    } elseif (file_get_contents($p_tarname, false, null, 1, 4) == '7zXZ') {
                        $this->_compress = true;
                        $this->_compress_type = 'lzma2';
                    }
                }
            } else {
                // probably a remote file or some file accessible
                // through a stream interface
                if (substr($p_tarname, -2) == 'gz') {
                    $this->_compress = true;
                    $this->_compress_type = 'gz';
                } elseif ((substr($p_tarname, -3) == 'bz2') ||
                    (substr($p_tarname, -2) == 'bz')
                ) {
                    $this->_compress = true;
                    $this->_compress_type = 'bz2';
                } else {
                    if (substr($p_tarname, -2) == 'xz') {
                        $this->_compress = true;
                        $this->_compress_type = 'lzma2';
                    }
                }
            }
        } else {
            if (($p_compress === true) || ($p_compress == 'gz')) {
                $this->_compress = true;
                $this->_compress_type = 'gz';
            } else {
                if ($p_compress == 'bz2') {
                    $this->_compress = true;
                    $this->_compress_type = 'bz2';
                } else {
                    if ($p_compress == 'lzma2') {
                        $this->_compress = true;
                        $this->_compress_type = 'lzma2';
                    } else {
                        $this->_error(
                            "Unsupported compression type '$p_compress'\n" .
                            "Supported types are 'gz', 'bz2' and 'lzma2'.\n"
                        );
                        return false;
                    }
                }
            }
        }
        $this->_tarname = $p_tarname;
        if ($this->_compress) { // assert zlib or bz2 or xz extension support
            if ($this->_compress_type == 'gz') {
                $extname = 'zlib';
            } else {
                if ($this->_compress_type == 'bz2') {
                    $extname = 'bz2';
                } else {
                    if ($this->_compress_type == 'lzma2') {
                        $extname = 'xz';
                    }
                }
            }

            if (!extension_loaded($extname)) {
                // Drupal change PEAR::loadExtension($extname).
                $this->loadExtension($extname);
            }
            if (!extension_loaded($extname)) {
                $this->_error(
                    "The extension '$extname' couldn't be found.\n" .
                    "Please make sure your version of PHP was built " .
                    "with '$extname' support.\n"
                );
                return false;
            }
        }


        if (version_compare(PHP_VERSION, "5.5.0-dev") < 0) {
            $this->_fmt = "a100filename/a8mode/a8uid/a8gid/a12size/a12mtime/" .
                "a8checksum/a1typeflag/a100link/a6magic/a2version/" .
                "a32uname/a32gname/a8devmajor/a8devminor/a131prefix";
        } else {
            $this->_fmt = "Z100filename/Z8mode/Z8uid/Z8gid/Z12size/Z12mtime/" .
                "Z8checksum/Z1typeflag/Z100link/Z6magic/Z2version/" .
                "Z32uname/Z32gname/Z8devmajor/Z8devminor/Z131prefix";
        }


        $this->buffer_length = $buffer_length;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
