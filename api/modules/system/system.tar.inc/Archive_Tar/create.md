# Archive_Tar::create()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 347–350 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L347-L350)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function create($p_filelist)
```

## Documentation

```text
This method creates the archive file and add the files / directories
that are listed in $p_filelist.
If a file with the same name exist and is writable, it is replaced
by the new tar.
The method return false and a PEAR error text.
The $p_filelist parameter can be an array of string, each string
representing a filename or a directory name with their path if
needed. It can also be a single string with names separated by a
single blank.
For each directory added in the archive, the files and
sub-directories are also added.
See also createModify() method for more details.

@param array $p_filelist An array of filenames and directory names, or a
             single string with names separated by a single
             blank space.

@return bool true on success, false on error.
@see    createModify()
```

## Code

```php
    public function create($p_filelist)
    {
        return $this->createModify($p_filelist, '', '');
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
