# HTML & Vanilla JavaScript code for all 12 interactive simulators

SIMULATORS = {
    "sim_01": """
    <div class="eco-card p-6 border-emerald-800/60">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900/60">
        <div>
          <h3 class="text-lg font-bold text-emerald-400">⚡ Planetary Decarbonization & Emissions Pathway Simulator (2020–2070)</h3>
          <p class="text-xs text-slate-300">Simulate India's and global emission trajectories under policy, technology, and clean energy interventions.</p>
        </div>
        <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Interactive Tool</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Renewable Energy Share by 2030 (%): <span id="val_re" class="text-emerald-400 font-bold">50%</span></label>
          <input type="range" id="input_re" min="20" max="80" value="50" class="w-full accent-emerald-500" oninput="runSim01()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Carbon Price ($/tonne CO₂): <span id="val_cp" class="text-emerald-400 font-bold">$35</span></label>
          <input type="range" id="input_cp" min="0" max="150" value="35" class="w-full accent-emerald-500" oninput="runSim01()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Energy Efficiency Improvement (%/yr): <span id="val_ee" class="text-emerald-400 font-bold">2.5%</span></label>
          <input type="range" id="input_ee" min="0.5" max="5.0" step="0.5" value="2.5" class="w-full accent-emerald-500" oninput="runSim01()">
        </div>
      </div>

      <!-- READOUTS -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-4">
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-3 text-center">
          <div class="text-[11px] text-slate-400 uppercase">2030 Emissions</div>
          <div id="out_2030" class="text-xl font-black text-emerald-400 mt-1">2.4 Gt CO₂</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-3 text-center">
          <div class="text-[11px] text-slate-400 uppercase">Year of Net-Zero</div>
          <div id="out_netzero" class="text-xl font-black text-teal-400 mt-1">2068</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-3 text-center">
          <div class="text-[11px] text-slate-400 uppercase">2100 Global Warming</div>
          <div id="out_warming" class="text-xl font-black text-amber-400 mt-1">+1.78 °C</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-3 text-center">
          <div class="text-[11px] text-slate-400 uppercase">Carbon Budget Used</div>
          <div id="out_budget" class="text-xl font-black text-cyan-400 mt-1">68%</div>
        </div>
      </div>

      <!-- DYNAMIC CANVAS -->
      <div class="bg-[#040806] border border-emerald-950 rounded-xl p-3">
        <div class="text-xs text-slate-400 mb-2 flex justify-between">
          <span>📉 Projected CO₂ Emissions Trajectory (2020 – 2070)</span>
          <span class="text-emerald-400 font-mono">Net-Zero Target Line: 0 Gt</span>
        </div>
        <canvas id="canvas_sim01" width="700" height="180" class="w-full h-44 rounded bg-[#030605]"></canvas>
      </div>
    </div>
    <script>
      function runSim01() {
        const re = parseFloat(document.getElementById('input_re').value);
        const cp = parseFloat(document.getElementById('input_cp').value);
        const ee = parseFloat(document.getElementById('input_ee').value);
        document.getElementById('val_re').innerText = re + '%';
        document.getElementById('val_cp').innerText = '$' + cp;
        document.getElementById('val_ee').innerText = ee + '%';

        const factor = (re * 0.4 + cp * 0.3 + ee * 10) / 100;
        const e2030 = Math.max(1.5, (3.2 - factor * 0.9)).toFixed(2);
        const netYear = Math.max(2045, Math.round(2085 - factor * 30));
        const warming = Math.max(1.4, (2.6 - factor * 1.1)).toFixed(2);
        const budget = Math.min(98, Math.max(45, Math.round(110 - factor * 45)));

        document.getElementById('out_2030').innerText = e2030 + ' Gt CO₂';
        document.getElementById('out_netzero').innerText = netYear <= 2070 ? netYear + ' (On Track!)' : netYear + ' (Delayed)';
        document.getElementById('out_warming').innerText = '+' + warming + ' °C';
        document.getElementById('out_budget').innerText = budget + '%';

        // Draw Canvas Chart
        const cvs = document.getElementById('canvas_sim01');
        if (!cvs) return;
        const ctx = cvs.getContext('2d');
        const W = cvs.width, H = cvs.height;
        ctx.clearRect(0, 0, W, H);

        // Grid lines
        ctx.strokeStyle = '#12261d';
        ctx.lineWidth = 1;
        for (let y = 30; y < H; y += 35) {
          ctx.beginPath(); ctx.moveTo(40, y); ctx.lineTo(W - 20, y); ctx.stroke();
        }

        // Target Line (0 Gt)
        const zeroY = H - 30;
        ctx.strokeStyle = '#ef4444';
        ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(40, zeroY); ctx.lineTo(W - 20, zeroY); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillStyle = '#ef4444'; ctx.font = '10px sans-serif'; ctx.fillText('0 Gt Net Zero', W - 85, zeroY - 6);

        // Trajectory
        ctx.beginPath();
        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 3;
        const startY = 40;
        ctx.moveTo(50, startY);

        const midX = 50 + (W - 100) * 0.2; // 2030
        const midY = 40 + (zeroY - 40) * (1 - (e2030 / 3.2));
        ctx.quadraticCurveTo(midX, midY - 10, midX, midY);

        const endX = 50 + (W - 100) * Math.min(1.0, (netYear - 2020) / 50);
        ctx.quadraticCurveTo((midX + endX) / 2, zeroY - 5, endX, zeroY);
        ctx.stroke();

        // Fill area under curve
        ctx.lineTo(50, zeroY);
        ctx.closePath();
        ctx.fillStyle = 'rgba(16, 185, 129, 0.08)';
        ctx.fill();

        // Labels
        ctx.fillStyle = '#94a3b8'; ctx.font = '10px sans-serif';
        ctx.fillText('2020 (3.2 Gt)', 40, H - 10);
        ctx.fillText('2030', midX - 12, H - 10);
        ctx.fillText('2050', 50 + (W - 100) * 0.6 - 12, H - 10);
        ctx.fillText('2070', W - 40, H - 10);
      }
      setTimeout(runSim01, 100);
    </script>
    """,

    "02": """
    <div class="eco-card p-6 border-emerald-800/60">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900/60">
        <div>
          <h3 class="text-lg font-bold text-emerald-400">🌐 Earth Radiation Budget & Greenhouse Equilibrium Calculator</h3>
          <p class="text-xs text-slate-300">Compute effective emitting temperature and surface greenhouse temperature by adjusting fundamental radiation parameters.</p>
        </div>
        <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Physics Model</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Solar Constant $S_0$ (W/m²): <span id="val_s0" class="text-emerald-400 font-bold">1361</span></label>
          <input type="range" id="input_s0" min="1200" max="1500" value="1361" class="w-full accent-emerald-500" oninput="runSim02()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Planetary Albedo $\\alpha$: <span id="val_albedo" class="text-emerald-400 font-bold">0.30</span></label>
          <input type="range" id="input_albedo" min="0.10" max="0.60" step="0.01" value="0.30" class="w-full accent-emerald-500" oninput="runSim02()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Atmospheric IR Emissivity $\\epsilon$: <span id="val_emissivity" class="text-emerald-400 font-bold">0.77</span></label>
          <input type="range" id="input_emissivity" min="0.00" max="0.99" step="0.01" value="0.77" class="w-full accent-emerald-500" oninput="runSim02()">
        </div>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-4">
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-3 text-center">
          <div class="text-[11px] text-slate-400 uppercase">Effective Temp ($T_e$)</div>
          <div id="out_te" class="text-xl font-black text-cyan-400 mt-1">255.0 K</div>
          <div id="out_te_c" class="text-[11px] text-slate-400">-18.2 °C</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-3 text-center">
          <div class="text-[11px] text-slate-400 uppercase">Surface Temp ($T_s$)</div>
          <div id="out_ts" class="text-xl font-black text-emerald-400 mt-1">288.2 K</div>
          <div id="out_ts_c" class="text-[11px] text-emerald-300 font-bold">+15.1 °C</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-3 text-center">
          <div class="text-[11px] text-slate-400 uppercase">Natural Greenhouse ΔT</div>
          <div id="out_gdelta" class="text-xl font-black text-amber-400 mt-1">+33.2 °C</div>
          <div class="text-[11px] text-slate-400">Thermal Blanket</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-3 text-center">
          <div class="text-[11px] text-slate-400 uppercase">Absorbed Solar Flux</div>
          <div id="out_absorbed" class="text-xl font-black text-teal-400 mt-1">238.2 W/m²</div>
          <div class="text-[11px] text-slate-400">$S_0(1-\\alpha)/4$</div>
        </div>
      </div>

      <div id="sim02_status" class="p-3 bg-[#0a1913] border border-emerald-800/80 rounded-xl text-xs text-emerald-200">
        💡 <strong>Earth Baseline:</strong> Under natural conditions ($S_0=1361, \\alpha=0.30, \\epsilon=0.77$), Earth's surface temperature is a hospitable 15°C. Increasing greenhouse gases raises $\\epsilon$, trapping extra infrared heat and elevating surface temperature.
      </div>
    </div>
    <script>
      function runSim02() {
        const S0 = parseFloat(document.getElementById('input_s0').value);
        const alpha = parseFloat(document.getElementById('input_albedo').value);
        const eps = parseFloat(document.getElementById('input_emissivity').value);
        document.getElementById('val_s0').innerText = S0;
        document.getElementById('val_albedo').innerText = alpha.toFixed(2);
        document.getElementById('val_emissivity').innerText = eps.toFixed(2);

        const sigma = 5.670374e-8;
        const absorbed = (S0 * (1 - alpha)) / 4.0;
        const Te = Math.pow(absorbed / sigma, 0.25);
        const Ts = Te * Math.pow(1.0 / (1.0 - eps / 2.0), 0.25);

        const Te_C = Te - 273.15;
        const Ts_C = Ts - 273.15;
        const delta = Ts_C - Te_C;

        document.getElementById('out_te').innerText = Te.toFixed(1) + ' K';
        document.getElementById('out_te_c').innerText = Te_C.toFixed(1) + ' °C';
        document.getElementById('out_ts').innerText = Ts.toFixed(1) + ' K';
        document.getElementById('out_ts_c').innerText = (Ts_C >= 0 ? '+' : '') + Ts_C.toFixed(1) + ' °C';
        document.getElementById('out_gdelta').innerText = '+' + delta.toFixed(1) + ' °C';
        document.getElementById('out_absorbed').innerText = absorbed.toFixed(1) + ' W/m²';
      }
      setTimeout(runSim02, 100);
    </script>
    """,

    "03": """
    <div class="eco-card p-6 border-emerald-800/60">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900/60">
        <div>
          <h3 class="text-lg font-bold text-emerald-400">🏭 Air Quality Index (AQI) & Plume Dispersion Calculator</h3>
          <p class="text-xs text-slate-300">Compute CPCB / US-EPA sub-indices for PM₂.₅ and PM₁₀ with Gaussian industrial chimney plume dispersion.</p>
        </div>
        <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Environmental Math</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">PM₂.₅ Concentration (μg/m³): <span id="val_pm25" class="text-emerald-400 font-bold">75</span></label>
          <input type="range" id="input_pm25" min="5" max="350" value="75" class="w-full accent-emerald-500" oninput="runSim03()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">PM₁₀ Concentration (μg/m³): <span id="val_pm10" class="text-emerald-400 font-bold">140</span></label>
          <input type="range" id="input_pm10" min="10" max="500" value="140" class="w-full accent-emerald-500" oninput="runSim03()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Wind Speed at Chimney (m/s): <span id="val_wind" class="text-emerald-400 font-bold">4.0</span></label>
          <input type="range" id="input_wind" min="1.0" max="12.0" step="0.5" value="4.0" class="w-full accent-emerald-500" oninput="runSim03()">
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Composite AQI Score</div>
          <div id="out_aqi" class="text-3xl font-black text-amber-400 my-1">150</div>
          <div id="out_category" class="inline-block px-3 py-0.5 rounded-full text-xs font-bold bg-amber-950 text-amber-300 border border-amber-800">Moderate</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Prominent Pollutant</div>
          <div id="out_dominant" class="text-xl font-bold text-emerald-400 my-1">PM₂.₅ (Fine Particles)</div>
          <div class="text-xs text-slate-400">Deep Alveolar Penetration</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Ground Downwind Peak Distance</div>
          <div id="out_dist" class="text-xl font-bold text-cyan-400 my-1">1.8 km</div>
          <div class="text-xs text-slate-400">Max Plume Touchdown</div>
        </div>
      </div>
      <div id="out_health" class="p-3 bg-[#11190f] border border-amber-800/80 rounded-xl text-xs text-amber-200">
        ⚠️ Breathing discomfort to people with lungs, asthma and heart diseases.
      </div>
    </div>
    <script>
      function calcSubAQI(val, breaks) {
        for (let b of breaks) {
          if (val <= b.ch) {
            return Math.round(((b.ih - b.il) / (b.ch - b.cl)) * (val - b.cl) + b.il);
          }
        }
        return 500;
      }
      function runSim03() {
        const pm25 = parseFloat(document.getElementById('input_pm25').value);
        const pm10 = parseFloat(document.getElementById('input_pm10').value);
        const wind = parseFloat(document.getElementById('input_wind').value);
        document.getElementById('val_pm25').innerText = pm25;
        document.getElementById('val_pm10').innerText = pm10;
        document.getElementById('val_wind').innerText = wind.toFixed(1);

        const pm25_breaks = [
          {cl:0, ch:30, il:0, ih:50},
          {cl:31, ch:60, il:51, ih:100},
          {cl:61, ch:90, il:101, ih:200},
          {cl:91, ch:120, il:201, ih:300},
          {cl:121, ch:250, il:301, ih:400},
          {cl:251, ch:500, il:401, ih:500}
        ];
        const pm10_breaks = [
          {cl:0, ch:50, il:0, ih:50},
          {cl:51, ch:100, il:51, ih:100},
          {cl:101, ch:250, il:101, ih:200},
          {cl:251, ch:350, il:201, ih:300},
          {cl:351, ch:430, il:301, ih:400},
          {cl:431, ch:600, il:401, ih:500}
        ];

        const aqi_25 = calcSubAQI(pm25, pm25_breaks);
        const aqi_10 = calcSubAQI(pm10, pm10_breaks);
        const aqi = Math.max(aqi_25, aqi_10);

        document.getElementById('out_aqi').innerText = aqi;
        document.getElementById('out_dominant').innerText = aqi_25 >= aqi_10 ? 'PM₂.₅ (Sub-AQI: ' + aqi_25 + ')' : 'PM₁₀ (Sub-AQI: ' + aqi_10 + ')';

        const cat = document.getElementById('out_category');
        const h = document.getElementById('out_health');
        if (aqi <= 50) {
          cat.innerText = 'Good'; cat.className = 'inline-block px-3 py-0.5 rounded-full text-xs font-bold bg-emerald-950 text-emerald-300 border border-emerald-800';
          h.innerText = '✅ Minimal health impact. Air quality is considered satisfactory.';
        } else if (aqi <= 100) {
          cat.innerText = 'Satisfactory'; cat.className = 'inline-block px-3 py-0.5 rounded-full text-xs font-bold bg-teal-950 text-teal-300 border border-teal-800';
          h.innerText = 'Minor breathing discomfort to sensitive people.';
        } else if (aqi <= 200) {
          cat.innerText = 'Moderate'; cat.className = 'inline-block px-3 py-0.5 rounded-full text-xs font-bold bg-amber-950 text-amber-300 border border-amber-800';
          h.innerText = '⚠️ Breathing discomfort to the people with lungs, asthma and heart diseases.';
        } else if (aqi <= 300) {
          cat.innerText = 'Poor'; cat.className = 'inline-block px-3 py-0.5 rounded-full text-xs font-bold bg-orange-950 text-orange-300 border border-orange-800';
          h.innerText = '🚨 Breathing discomfort to most people on prolonged exposure.';
        } else {
          cat.innerText = 'Severe / Hazardous'; cat.className = 'inline-block px-3 py-0.5 rounded-full text-xs font-bold bg-red-950 text-red-300 border border-red-800';
          h.innerText = '⛔ Emergency conditions. Serious risk of respiratory effects in general population.';
        }

        const dist = (7.2 / wind).toFixed(1);
        document.getElementById('out_dist').innerText = dist + ' km';
      }
      setTimeout(runSim03, 100);
    </script>
    """,

    "04": """
    <div class="eco-card p-6 border-emerald-800/60">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900/60">
        <div>
          <h3 class="text-lg font-bold text-emerald-400">🛰️ Multispectral Remote Sensing & NDVI Vegetation Index Visualizer</h3>
          <p class="text-xs text-slate-300">Simulate spectral reflectance in Red and NIR bands, calculate NDVI, and determine land cover classification.</p>
        </div>
        <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Remote Sensing</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Red Reflectance (ρ_Red): <span id="val_red" class="text-red-400 font-bold">0.06</span></label>
          <input type="range" id="input_red" min="0.01" max="0.60" step="0.01" value="0.06" class="w-full accent-red-500" oninput="runSim04()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Near-Infrared Reflectance (ρ_NIR): <span id="val_nir" class="text-emerald-400 font-bold">0.52</span></label>
          <input type="range" id="input_nir" min="0.01" max="0.75" step="0.01" value="0.52" class="w-full accent-emerald-500" oninput="runSim04()">
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Calculated NDVI</div>
          <div id="out_ndvi" class="text-3xl font-black text-emerald-400 my-1">+0.79</div>
          <div class="text-xs text-slate-400">Formula: (NIR - Red)/(NIR + Red)</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Classified Land Cover</div>
          <div id="out_landcover" class="text-lg font-bold text-emerald-300 my-1">Dense Healthy Forest</div>
          <div id="out_lai" class="text-xs text-slate-400">Leaf Area Index (LAI): High</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Standard FCC Display Appearance</div>
          <div id="out_fcc_color" class="h-8 rounded-lg my-1 border border-white/20 flex items-center justify-center font-bold text-xs" style="background:#dc2626; color:white;">Bright Crimson Red</div>
          <div class="text-xs text-slate-400">NIR mapped to Red Channel</div>
        </div>
      </div>
    </div>
    <script>
      function runSim04() {
        const r = parseFloat(document.getElementById('input_red').value);
        const nir = parseFloat(document.getElementById('input_nir').value);
        document.getElementById('val_red').innerText = r.toFixed(2);
        document.getElementById('val_nir').innerText = nir.toFixed(2);

        const ndvi = (nir - r) / (nir + r);
        document.getElementById('out_ndvi').innerText = (ndvi >= 0 ? '+' : '') + ndvi.toFixed(2);

        const lc = document.getElementById('out_landcover');
        const lai = document.getElementById('out_lai');
        const fcc = document.getElementById('out_fcc_color');

        if (ndvi < -0.1) {
          lc.innerText = 'Deep Water / Ocean';
          lai.innerText = 'Zero Chlorophyll absorption';
          fcc.style.background = '#0284c7'; fcc.innerText = 'Deep Blue / Black';
        } else if (ndvi < 0.1) {
          lc.innerText = 'Barren Rock / Sandy Soil';
          lai.innerText = 'Minimal vegetative cover';
          fcc.style.background = '#94a3b8'; fcc.innerText = 'Cyan / Grey';
        } else if (ndvi < 0.35) {
          lc.innerText = 'Sparse Grassland / Shrub';
          lai.innerText = 'Moderate vegetative activity';
          fcc.style.background = '#f87171'; fcc.innerText = 'Light Pink / Orange';
        } else if (ndvi < 0.65) {
          lc.innerText = 'Moderate Canopy / Crops';
          lai.innerText = 'Healthy growing season';
          fcc.style.background = '#ef4444'; fcc.innerText = 'Red';
        } else {
          lc.innerText = 'Dense Tropical Forest Canopy';
          lai.innerText = 'High Leaf Area Index (LAI > 4)';
          fcc.style.background = '#b91c1c'; fcc.innerText = 'Deep Crimson Red';
        }
      }
      setTimeout(runSim04, 100);
    </script>
    """
}

print("Simulators 1-4 loaded.")
