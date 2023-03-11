<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <!-- Boxicons input -->
    <link href='https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css' rel='stylesheet'>  
    <!-- Bootstrap CSS -->
    <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi' crossorigin='anonymous'>
    <!-- Latest compiled and minified JavaScript -->
    <script
       src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <!-- Css -->
    <meta name="viewport" content="width=device-width, initial-scale=2.0">
    <link rel="stylesheet" href="css/style.css">
    <!-- Vue 3 -->
    <script src='https://unpkg.com/vue@next'></script>

    <!-- Axios -->
    <script src='https://unpkg.com/axios/dist/axios.min.js'></script>
    
    <title>Shoppinger start</title>
</head>
<body>
    <header class="primary-header">
        <nav class="nav bd-grid">
            <div>
                <a href="#home" class="nav__logo">TCM</a>
            </div>
            <div class="nav__menu" id="nav-menu">
                <ul class="nav__list">
                    <li class="nav__item"><a href="#home" class="nav__links active">Home</a></li>
                    <li class="nav__item"><a href="#featured" class="nav__links">Consultations</a></li>
                    <li class="nav__item">New<a href="#new" class="nav__links">Prescriptions</a></li>
                    <li class="nav__item"><a href="#subscribe" class="nav__links">Log Out</a></li>
                </ul>
            </div>
            <div>
                <i class="bx bxs-cart-add nav__cart"></i>
                <i class="bx bx-menu-alt-right nav__toggle" id="nav-toggle"></i>
            </div>
        </nav>
    </header>

    <main>      
        <!-- Home -->
        <section class="home" id="home">
            
            <div class="home__container bd-grid">
                <div class="home__data">
                    <div class="" id="app">
                        <!-- d-flex align-items-{center / start / end} justify-content-{center / start / end} -->
                        <!-- None  <576px, sm  >=576px, md  >=768px, lg  >=992px, xl  >=1200px, xxl  >=1400px -->
                        <!-- m-1 : 4px, m-2 : 8px, m-3 : 16px, m-4 : 24px, m-5 : 48px -->
                        <div class='container-fluid'>
                            <div class='row mb-3'>
                                <div class='col p-0'>

                                    <!-- Consultation Bar -->
                                    
                                    <h1 class="">
                                        <span class="secondary button">Consultations</span> 
                                        <span class="">> Prescription</span>
                                    </h1>

                                    <div class="container-fluid">
                                        <div class='col'>
                                            consulatation bar
                                            
                                        </div> <!-- col -->
                                    </div> <!-- container-->

                                </div> <!-- col -->
                            </div> <!-- row -->

                            <div class='row mb-3'>
                                <div class='col p-0'>
                                    <h2>Upcoming</h2>
                                    <span class="">Upcoming consultations</span> 

                                    <div class="container-fluid">
                                        <div class="row">
                                            <div class='col-3'>
                                                <div class="bg-info bg-opacity-10 border border-info rounded text-center"> 
                                                    <h3>21</h3> <strong>Mar</strong> <p>2023</p>
                                                </div>                                            
                                            </div> <!-- col -->
                                            <div class='col'>
                                                <strong>Tanah Merah Outlet</strong>
                                                <div>Tue, 02:30PM</div>
                                                <div>DR LI HANYI</div>                                      
                                            </div> <!-- col -->
                                            <div class='col'>
                                                <button type='button' class='btn btn-primary'>Reschedule</button>              
                                                <button type='button' class='btn btn-primary'>Cancel</button>              
                                            </div> <!-- col -->
                                        </div>
                                        
                                    </div> <!-- container-->

                                </div> <!-- col -->
                            </div> <!-- row -->

                            <div class='row '>
                                <div class='col p-0'>
                                    <h2>Past Sessions</h2>
                                    <patientinfo
                                            :patients="patients"
                                            >
                                    </patientinfo>

                                    <pastsession>
                                    </pastsession>
                                    


                                    <!-- <table class='table table-white table-hover table-bordered no-more-tables'>
                                        <thead>
                                            <tr>
                                                <th scope='col-1'>Date</th>
                                                <th scope='col'>Order ID</th>
                                                <th scope='col'>3</th>
                                                <th scope='col'>Price</th>
                                                <th scope='col'>Status</th>
                                            </tr>
                                        </thead>
                                        <tbody class='table-group-divider'>
                                            <tr>
                                                <td data-title="Date">08/03/23</td>
                                                <td data-title="Order ID">asd</td>
                                                <td >asdasdasdasdasdasdasadasddasddasddasddasdasdada</td>
                                                <td data-title="Price">$100</td>
                                                <td data-title="Status"> <button type='button' class='btn btn-primary'>Make Payment</button> </td>
                                            </tr>
                                        
                                            <tr>
                                                <th scope='row'></th>
                                                <td></td>
                                                <td></td>
                                            </tr>
                                        </tbody>
                                    </table> -->


                                </div> <!-- col -->
                            </div> <!-- row -->
                        </div> <!-- container -->
                    </div> <!-- vue -->
                </div>
                <!-- <a href="#featured" class="button">Go &rarr;</a> -->
                <!-- <img src="img/home.png" alt="" class="home__img"> -->
            </div>
        </section>
    </main>
        
    <script src="js/patient.js"></script>
    <script src="js/script.js"></script>
    <!-- Bootstrap Javascript -->
    <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js' integrity='sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3' crossorigin='anonymous'></script>
</body>
</html>