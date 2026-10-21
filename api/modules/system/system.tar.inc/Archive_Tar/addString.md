# Archive_Tar::addString()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 562–590 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L562-L590)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function addString($p_filename, $p_string, $p_datetime = false, $p_params = array())
```

## Documentation

```text
This method add a single string as a file at the
end of the existing archive. If the archive does not yet exists it
is created.

@param string $p_filename A string which contains the full
                          filename path that will be associated
                          with the string.
@param string $p_string The content of the file added in
                          the archive.
@param bool|int $p_datetime A custom date/time (unix timestamp)
                          for the file (optional).
@param array $p_params An array of optional params:
                              stamp => the datetime (replaces
                                  datetime above if it exists)
                              mode => the permissions on the
                                  file (600 by default)
                              type => is this a link?  See the
                                  tar specification for details.
                                  (default = regular file)
                              uid => the user ID of the file
                                  (default = 0 = root)
                              gid => the group ID of the file
                                  (default = 0 = root)

@return bool true on success, false on error.
```

## Code

```php
    public function addString($p_filename, $p_string, $p_datetime = false, $p_params = array())
    {
        $p_stamp = @$p_params["stamp"] ? $p_params["stamp"] : ($p_datetime ? $p_datetime : time());
        $p_mode = @$p_params["mode"] ? $p_params["mode"] : 0600;
        $p_type = @$p_params["type"] ? $p_params["type"] : "";
        $p_uid = @$p_params["uid"] ? $p_params["uid"] : "";
        $p_gid = @$p_params["gid"] ? $p_params["gid"] : "";
        $v_result = true;

        if (!$this->_isArchive()) {
            if (!$this->_openWrite()) {
                return false;
            }
            $this->_close();
        }

        if (!$this->_openAppend()) {
            return false;
        }

        // Need to check the get back to the temporary file ? ....
        $v_result = $this->_addString($p_filename, $p_string, $p_datetime, $p_params);

        $this->_writeFooter();

        $this->_close();

        return $v_result;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
