# Archive_Tar::_addString()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1366–1411 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1366-L1411)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _addString($p_filename, $p_string, $p_datetime = false, $p_params = array())
```

## Documentation

```text
@param string $p_filename
@param string $p_string
@param bool $p_datetime
@param array $p_params
@return bool
```

## Code

```php
    public function _addString($p_filename, $p_string, $p_datetime = false, $p_params = array())
    {
        $p_stamp = @$p_params["stamp"] ? $p_params["stamp"] : ($p_datetime ? $p_datetime : time());
        $p_mode = @$p_params["mode"] ? $p_params["mode"] : 0600;
        $p_type = @$p_params["type"] ? $p_params["type"] : "";
        $p_uid = @$p_params["uid"] ? $p_params["uid"] : 0;
        $p_gid = @$p_params["gid"] ? $p_params["gid"] : 0;
        if (!$this->_file) {
            $this->_error('Invalid file descriptor');
            return false;
        }

        if ($p_filename == '') {
            $this->_error('Invalid file name');
            return false;
        }

        // ----- Calculate the stored filename
        $p_filename = $this->_translateWinPath($p_filename, false);

        // ----- If datetime is not specified, set current time
        if ($p_datetime === false) {
            $p_datetime = time();
        }

        if (!$this->_writeHeaderBlock(
            $p_filename,
            strlen($p_string),
            $p_stamp,
            $p_mode,
            $p_type,
            $p_uid,
            $p_gid
        )
        ) {
            return false;
        }

        $i = 0;
        while (($v_buffer = substr($p_string, (($i++) * 512), 512)) != '') {
            $v_binary_data = pack("a512", $v_buffer);
            $this->_writeBlock($v_binary_data);
        }

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
