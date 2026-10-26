# Tiffany M. Mui
# Module 6 Assignment - Testing
# CSCI-3025: Python Programming
# Purpose: Helper functions that are shared across tests


from datetime import datetime, timedelta


def offset_date(**kwargs):
    """Returns a relative date from now to ensure past and future
    
    Args:
        **kwargs: any combination accepted by datetime.timedelta
    
    Returns:
        rel_dtg: datetime value that is offset from now
    """
    rel_dtg = datetime.now() + timedelta(**kwargs)
    return rel_dtg
