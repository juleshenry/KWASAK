# -*- coding: utf-8 -*-
"""
Created on Mon May  8 10:56:16 CDT 2023

@author: Julian Henry

Allows for arbitrary missing variable resolution

Working examples. Wed May 24 22:19:54 CDT 2023


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%^^^^^%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^%%^^^^^%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%^^^^^%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^%%^^^^^%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%^^^^^%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^%%^^^^^%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%^^^^^%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%^^^^^%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^%%^^^^^%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%^^^^^%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%^^^^%%%%%%%%%%%%%%^^^^%^^^^^^^^%%%%%%%%%%^^^^^^^^^%%%%%%^^^^%^^^^^^^^%%%%%^^^^%^^^^^^^^%%%%%^^^^^%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%^^^^^^^^%%^^^^%%^^^^%%%%%%%^^^^^^^^%%^^^^%%%%%%%%%%%%%^^^^%%%^^^^^^^^^^%%%%%%%%%%%%%^^^^^^^^^^%%%%%%^^^^^^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^%%%%%%^^^^%^^^^^^^^%%%%^^^^^^^^%%%%
%%%^^^^%%%%%%%%%%%%%%^^^^^^^^^^^^^^%%%%%%%^^^^^^^^^^^^%%%%%^^^^^^^^^^^^^^%%%%^^^^^^^^^^^^^^%%%%^^^^^^%%%%%%%^^^^^%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^%%^^^^%%%%%%^^^^^^^^^^^^^^^%%%%%%%%%%%%%^^^^%%%^^^^^^^^^^%%%%%%%%%%%%%^^^^^^^^^^%%%%%^^^^^^^^^^^^%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^%%%%%^^^^^^^^^^^^^^%%^^^^^^^^^^^%%
%%%^^^^%%%%%%%%%%%%%%^^^^^^^^^^^^^^^%%%%%^^^^^^^^^^^^^^%%%%^^^^^^^^^^^^^^^%%%^^^^^^^^^^^^^^^%%%%^^^^^%%%%%%%^^^^^%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^%%^^^^%%%%%^^^^^^^^^^^^^^^^%%%%%%%%%%%%%^^^^%%%^^^^^^^^^^%%%%%%%%%%%%%^^^^^^^^^^%%%%^^^^^^^^^^^^^^%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^%%%%^^^^^^^^^^^^^^^^^^^^^^^^^^^%%
%%%^^^^%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^%%%^^^^^^^^^^^^^^^^%%%^^^^^^^^^^^^^^^^%%^^^^^^^^^^^^^^^^%%%^^^^^%%%%%%%^^^^%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^%%^^^^%%%%^^^^^^^^^^^^^^^^^%%%%%%%%%%%%%^^^^%%%^^^^^^^^^^%%%%%%%%%%%%%^^^^^^^^^^%%%^^^^^^^^^^^^^^^^%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^%%%^^^^^^^^^^^^^^^^^^^^^^^^^^^^%
%%%^^^^%%%%%%%%%%%%%%^^^^^^%%%%^^^^^^%%%^^^^^^%%%%%^^^^^^%%^^^^^^%%%%^^^^^^%%^^^^^^%%%%^^^^^^%%%^^^^^^%%%%%^^^^^%%%%%%%%%%%%%%%^^^^^^^%%%%^^^^^^^%%^^^^%%%^^^^^^^%%%%^^^^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%^^^^^^^%%%%^^^^^^^%%%%%%%%%%%%%%%%%%%^^^^^^%%%%%^^^^^^%%^^^^^^%%%%^^^^^^^^%%%%%^^^^^%
%%%^^^^%%%%%%%%%%%%%%^^^^^%%%%%%^^^^^%%^^^^^^%%%%%%%^^^^^%%^^^^^%%%%%%^^^^^%%^^^^^%%%%%%^^^^^%%%%^^^^^%%%%%^^^^^%%%%%%%%%%%%%%%^^^^^^%%%%%%^^^^^^%%^^^^%%%^^^^^^%%%%%%^^^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%^^^^^%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%^^^^^^%%%%%%%^^^^^%%^^^^^%%%%%%^^^^^^%%%%%%^^^^^^
%%%^^^^%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%^^^^^%%%%%%%%^^^^^%%^^^^%%%%%%%%^^^^%%^^^^%%%%%%%%^^^^%%%%^^^^^%%%%^^^^^%%%%%%%%%%%%%%%%^^^^^%%%%%%%%^^^^^%%^^^^%%%^^^^^%%%%%%%%^^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%^^^^^%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%^^^^^%%^^^^%%%%%%%%^^^^^%%%%%%%^^^^^
%%%^^^^%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%^^^^^^^^^^^^^^^^^^%%^^^^%%%%%%%%^^^^%%^^^^%%%%%%%%^^^^%%%%%^^^^^%%%^^^^^%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%^^^^%%^^^^%%%^^^^%%%%%%%%%%^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%^^^^%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^%%^^^^%%%%%%%%^^^^^%%%%%%%^^^^^
%%%^^^^%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%^^^^^^^^^^^^^^^^^^%%^^^^%%%%%%%%^^^^%%^^^^%%%%%%%%^^^^%%%%%^^^^^%%%^^^^%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%^^^^%%^^^^%%%^^^^%%%%%%%%%%^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%^^^^%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^%%^^^^%%%%%%%%^^^^%%%%%%%%^^^^^
%%%^^^^%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%^^^^^^^^^^^^^^^^^^%%^^^^%%%%%%%%^^^^%%^^^^%%%%%%%%^^^^%%%%%^^^^^^%^^^^^%%%%%%%%%%%%%%%%%^^^^%%%%%%%%%%^^^^%%^^^^%%%^^^^%%%%%%%%%%^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%^^^^%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^%%^^^^%%%%%%%%^^^^%%%%%%%%^^^^^
%%%^^^^%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%^^^^^^^^^^^^^^^^^^%%^^^^%%%%%%%%^^^^%%^^^^%%%%%%%%^^^^%%%%%%^^^^^%^^^^^%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%%^^^^%%^^^^%%%^^^^^%%%%%%%%%^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%^^^^%%%%%%%%%%^^^^%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^^%%^^^^%%%%%%%%^^^^%%%%%%%%^^^^^
%%%^^^^%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%^^^^^%%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%^^^^%%%%%%%%^^^^%%%%%%^^^^^^^^^^%%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%^^^^^%%^^^^%%%^^^^^%%%%%%%%^^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%^^^^^%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%%%%%%%^^^^^
%%%^^^^%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%^^^^^^%%%%%%%^^^^^%%^^^^%%%%%%%%^^^^%%^^^^%%%%%%%%^^^^%%%%%%%^^^^^^^^^%%%%%%%%%%%%%%%%%%^^^^^^%%%%%%^^^^^^%%^^^^%%%^^^^^^%%%%%%^^^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%^^^^^%%%%%%%^^^^^^%%%%%%%%%%%%%%%%%%^^^^^^%%%%%%%^^^^^%%^^^^%%%%%%%%^^^^%%%%%%%%^^^^^
%%%^^^^%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%%^^^^^^%%%%%^^^^^%%%^^^^%%%%%%%%^^^^%%^^^^%%%%%%%%^^^^%%%%%%%^^^^^^^^%%%%%%%%%%%%%%%%%%%^^^^^^^%%%%^^^^^^^%%^^^^%%%^^^^^^^%%%%^^^^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^%%%%%%%%%%%%%%%%%%%^^^^%%%%%%^^^^^^%%%%%^^^^^^^%%%%%%%%%%%%%%%%%%%^^^^^^%%%%%^^^^^%%%^^^^%%%%%%%%^^^^%%%%%%%%^^^^^
%%%^^^^%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%%^^^^^^^^^^^^^^^^%%%^^^^%%%%%%%%^^^^%%^^^^%%%%%%%%^^^^%%%%%%%^^^^^^^^%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^^%%^^^^%%%%^^^^^^^^^^^^^^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^^^^^%%%%%%%%%%%%%%%^^^^^^^^%%%^^^^^^^^^^^^^^^^%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^%%%^^^^%%%%%%%%^^^^%%%%%%%%^^^^^
%%%^^^^%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%%%^^^^^^^^^^^^^^%%%%^^^^%%%%%%%%^^^^%%^^^^%%%%%%%%^^^^%%%%%%%%^^^^^^%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^^%%^^^^%%%%%^^^^^^^^^^^^^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^^^^^%%%%%%%%%%%%%%%^^^^^^^^%%%%^^^^^^^^^^^^^^%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^%%%%^^^^%%%%%%%%^^^^%%%%%%%%^^^^^
%%%^^^^%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%%%%^^^^^^^^^^^^%%%%%^^^^%%%%%%%%^^^^%%^^^^%%%%%%%%^^^^%%%%%%%%^^^^^^%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^^^^%%^^^^%%%%%%^^^^^^^^^^^^^^^%%%%%%%%%%%%%^^^^%%%%%^^^^^^^^%%%%%%%%%%%%%%%^^^^^^^^%%%%%^^^^^^^^^^^^%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^^^^%%%%%^^^^%%%%%%%%^^^^%%%%%%%%^^^^^
%%%^^^^%%%%%%%%%%%%%%^^^^%%%%%%%%^^^^%%%%%%%^^^^^^^^^%%%%%%^^^^%%%%%%%%^^^^%%^^^^%%%%%%%%^^^^%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^%%^^^^%%^^^^%%%%%%%^^^^^^^^%%^^^^%%%%%%%%%%%%%^^^^%%%%%%^^^^^^^%%%%%%%%%%%%%%%%^^^^^^^%%%%%%^^^^^^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^^^^%%%%%%^^^^%%%%%%%%^^^^%%%%%%%%^^^^^
%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
^^^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
^^^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
^^^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
^^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%^^^^^%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Fri Jul 28 20:37:55 CDT 2023
Published.
"""
import inspect


def kwasak(func):
    """
    Intention:
    base method is `vanilla`... that means no `__syntax`

    and can calculate necessary formula to solve for a single variable

    Assumption: method is not static. why? we abuse inspect to inspect the
    [1:-1] kwargs in order to resolve the missing parameter
    """

    def wrapper(self, **kwargs):
        method_name = func.__name__
        all_parameters = list(inspect.signature(func).parameters)[1:-1]
        missing_arg = [kw for kw in all_parameters if kw not in kwargs]
        if not len(missing_arg) == 1:
            raise ValueError(
                "Must have exactly one missing variable for which to solve."
            )
        correct_method = method_name + "__" + missing_arg[0]
        correct_args = [x[1] for x in sorted(kwargs.items(), key=lambda kv: kv[0])]
        return getattr(self, correct_method)(*correct_args)

    return wrapper
